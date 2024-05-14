const { default: Decimal } = require("decimal.js");
Decimal.set({ precision: 28 }); // Set precision to 30 significant digits

// Define the global variables
let text = null;
let textSize = 5;
// let textSize = 5000;

let degrees = [2, 3, 4, 5, 6];
let polynomials = [];
let encryptionTime = [];
let decryptionTime = [];
let totalTime = [];

// Define the global functions
function getRandom8Chars(charsLength, nSamples) {
  let randomChars = "";
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  for (let i = 0; i < nSamples; i++) {
    for (let j = 0; j < charsLength; j++) {
      randomChars += letters.charAt(Math.floor(Math.random() * letters.length));
    }
  }
  return randomChars;
}

class BiNew {
  constructor(text, x, y) {
    if (typeof text !== "string" || x.length !== y.length) {
      throw new Error("Invalid Parameters");
    }
    this.text = text;
    this.len_text = text.length;
    this.x = x.map((i) => new Decimal(i));
    this.y = y.map((i) => new Decimal(i));
    this.coefs = null;
    this.maximium_8utf_chars = new Decimal("597351581456640298090110");
    this.minimum_8utf_chars = new Decimal("151708338147718170943520");
    this.len_x = x.length;
  }

  set_text(text) {
    if (typeof text !== "string") {
      throw new Error("Invalid text type passed");
    }
    this.text = text;
  }

  set_x_y(x, y) {
    if (x.length !== y.length) {
      throw new Error("Invalid x, y points size passed");
    }
    this.x = x.map((i) => new Decimal(i));
    this.y = y.map((i) => new Decimal(i));
    this.len_x = x.length;
    this.coefs = null;
  }

  encode_and_get_int_values(chunk) {
    const byteRepresentation = new TextEncoder().encode(chunk);
    let integerRepresentation = new Decimal(0);
    byteRepresentation.forEach((byte, index) => {
      integerRepresentation = integerRepresentation.plus(
        new Decimal(byte).times(
          new Decimal(256).pow(byteRepresentation.length - index - 1)
        )
      );
    });
    return integerRepresentation.toString();
  }

  get_normalized_value(integerValue) {
    let decimalValue = new Decimal(integerValue);
    let normalizedValue = decimalValue
      .minus(this.minimum_8utf_chars)
      .div(this.maximium_8utf_chars.minus(this.minimum_8utf_chars));
    return normalizedValue;
  }

  get_inverse_normalized_value(normalizedValue) {
    let integerValue = new Decimal(normalizedValue)
      .times(this.maximium_8utf_chars.minus(this.minimum_8utf_chars))
      .plus(this.minimum_8utf_chars);
    return integerValue;
  }

  get_normalized_values() {
    let normalizedValues = [];
    let chunks = Math.floor(this.len_text / 10);
    let beg = 0,
      end = 0;
    if (chunks) {
      end = 10;
      for (let i = 0; i < chunks; i++) {
        let chunk = this.text.substring(beg, end);
        normalizedValues.push(
          this.get_normalized_value(this.encode_and_get_int_values(chunk))
        );
        beg = end;
        end = beg + 10;
      }
    }
    if ((this.len_text / 10) % 1 !== 0) {
      let chunk = this.text.substring(end);
      normalizedValues.push(
        this.get_normalized_value(this.encode_and_get_int_values(chunk))
      );
    }
    return normalizedValues;
  }

  get_interger_values(normalizedValues) {
    let intergerValues = [];
    for (let normalizedValue of normalizedValues) {
      intergerValues.push(this.get_inverse_normalized_value(normalizedValue));
    }
    return intergerValues;
  }

  decode_and_get_string(intValue) {
    intValue = Math.ceil(new Decimal(intValue).toNumber());
    let byteRepresentation = new Uint8Array(
      (intValue.toString(2).length + 7) >> 3
    );
    for (let index = byteRepresentation.length - 1; index >= 0; index--) {
      byteRepresentation[index] = intValue & 0xff;
      intValue >>= 8;
    }
    let decoder = new TextDecoder();
    return decoder.decode(byteRepresentation);
  }
  // ===============================
  newton_forward_coefficients() {
    const n = this.x.length;
    let coefficients = new Array(n).fill(new Decimal(0));
    for (let i = 0; i < n; i++) {
      coefficients[i] = new Decimal(this.y[i]);
    }
    for (let j = 1; j < n; j++) {
      for (let i = n - 1; i >= j; i--) {
        coefficients[i] = coefficients[i]
          .minus(coefficients[i - 1])
          .div(this.x[i].minus(this.x[i - j]));
      }
    }
    this.coefs = coefficients;
  }

  evaluate_interpolated_value(target, normalized_value = new Decimal(0)) {
    const n = this.len_x;
    let result = new Decimal(this.coefs[n - 1]);
    for (let i = n - 2; i >= 0; i--) {
      result = result
        .times(new Decimal(target).minus(this.x[i]))
        .plus(this.coefs[i]);
    }
    return result.minus(normalized_value);
  }

  bisection_method(
    a,
    b,
    normalized_value,
    tol = new Decimal(Math.pow(10, -38))
  ) {
    if (
      this.evaluate_interpolated_value(a, normalized_value).times(
        this.evaluate_interpolated_value(b, normalized_value)
      ) > 0
    ) {
      throw new Error(
        "The function values at the endpoints must have different signs."
      );
    }
    let midpoint;
    for (let i = 0; i < 40; i++) {
      midpoint = new Decimal(a).plus(b).div(2);
      if (
        this.evaluate_interpolated_value(midpoint, normalized_value).equals(0)
      ) {
        return midpoint;
      } else if (
        this.evaluate_interpolated_value(midpoint, normalized_value).times(
          this.evaluate_interpolated_value(a, normalized_value)
        ) < 0
      ) {
        b = midpoint;
      } else {
        a = midpoint;
      }
    }
    return midpoint;
  }
}
