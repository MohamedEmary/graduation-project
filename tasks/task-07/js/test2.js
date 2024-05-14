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
    this.maximium_8utf_chars = new Decimal("139081753198206");
    this.minimum_8utf_chars = new Decimal("35322350018592");
    this.len_x = x.length;
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
    let chunks = Math.floor(this.len_text / 6);
    let beg = 0,
      end = 0;
    if (chunks) {
      end = 6;
      for (let i = 0; i < chunks; i++) {
        let chunk = this.text.substring(beg, end);
        normalizedValues.push(
          this.get_normalized_value(this.encode_and_get_int_values(chunk))
        );
        beg = end;
        end = beg + 6;
      }
    }
    if ((this.len_text / 6) % 1 !== 0) {
      let chunk = this.text.substring(beg);
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
    intValue = Decimal.ceil(intValue);
    let byteLength = Math.ceil(intValue.log(256));
    let byteRepresentation = [];

    for (let i = byteLength - 1; i >= 0; i--) {
      let byte = intValue.div(Decimal.pow(256, i)).floor();
      byteRepresentation.push(byte.toNumber());
      intValue = intValue.minus(byte.times(Decimal.pow(256, i)));
    }

    const textDecoder = new TextDecoder("utf-8");
    return textDecoder.decode(new Uint8Array(byteRepresentation));
  }

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

  find_roots_secant(
    x0,
    x1,
    normalized_value,
    tol = new Decimal(Math.pow(10, -17)),
    max_iter = 16
  ) {
    let x_prev = new Decimal(x0);
    let x_curr = new Decimal(x1);
    for (let i = 0; i < max_iter; i++) {
      let fx_prev = this.evaluate_interpolated_value(x_prev, normalized_value);
      let fx_curr = this.evaluate_interpolated_value(x_curr, normalized_value);
      if (fx_curr.minus(fx_prev).equals(0)) {
        throw new Error("Secant method cannot converge. Division by zero.");
      }
      let x_next = x_curr.minus(
        fx_curr.times(x_curr.minus(x_prev)).div(fx_curr.minus(fx_prev))
      );
      x_prev = x_curr;
      x_curr = x_next;
      if (fx_curr.abs().lessThan(tol)) {
        return x_curr;
      }
    }
    return x_curr;
  }

  encryption() {
    let cipher_text = [];
    this.newton_forward_coefficients();
    let normalized_values = this.get_normalized_values();
    for (let normalized_value of normalized_values) {
      cipher_text.push(
        this.find_roots_secant(
          this.x[0],
          this.x[this.len_x - 1],
          normalized_value
        )
      );
    }
    return cipher_text;
  }

  decryption(cipher_text) {
    let text = [];
    for (let root of cipher_text) {
      let norm = this.evaluate_interpolated_value(root);
      let inverse = this.get_inverse_normalized_value(norm);
      text.push(this.decode_and_get_string(Math.round(inverse.toNumber())));
    }
    return text.join("");
  }
}

text = "kaVELmZdFztIZKgNwVtmIlERBwnlNLQBxpRcezrbbwladouabfuawvfiyawvjLpghbwJg";
let xpoints = [17, 17.5, 18.0, 18.5, 19.0, 19.5];
let ypoints = [45, 45.5, 46.0, -46.5, -47.0, -47.5];

let obj = new BiNew(text, xpoints, ypoints);
let ciper_text = obj.encryption();
let decrypted_text = obj.decryption(ciper_text);
console.log(decrypted_text);
console.log(text === decrypted_text);
