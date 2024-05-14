function set_text(text) {
  if (typeof text !== "string") {
    throw new Error("Invalid text type passed");
  }
  this.text = text;
}

function set_x_y(x, y) {
  if (x.length !== y.length) {
    throw new Error("Invalid x, y points size passed");
  }
  this.x = x.map((i) => new Decimal(i));
  this.y = y.map((i) => new Decimal(i));
  this.len_x = x.length;
  this.coefs = null;
}

function bisection_method(
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
