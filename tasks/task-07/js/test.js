const { default: Decimal } = require("decimal.js");
Decimal.set({ precision: 28 });

function decode_and_get_string(intValue) {
  intValue = new Decimal(intValue);
  let byteRepresentation = [];

  while (intValue.greaterThan(0)) {
    let byte = intValue.mod(256);
    byteRepresentation.unshift(byte.toNumber());
    intValue = intValue.dividedToIntegerBy(256);
  }

  const textDecoder = new TextDecoder("utf-8");

  console.log(byteRepresentation); // [107, 97, 86, 69, 76, 109, 92, 32, 167, 0]
  // it should be [107, 97, 86, 69, 76, 109, 90, 100, 70, 122]

  return textDecoder.decode(new Uint8Array(byteRepresentation));
}

console.log(decode_and_get_string("5.070887643010951e+23")); // kaVELmZdFz

// kaVELmZdFz
// k: ASCII code point 107
// a: ASCII code point 97
// V: ASCII code point 86
// E: ASCII code point 69
// L: ASCII code point 76
// m: ASCII code point 109
// Z: ASCII code point 90
// d: ASCII code point 100
// F: ASCII code point 70
// z: ASCII code point 122

/* 
console.log(decode_and_get_string("5.070887643010951e+23")); // kaVELmZdFz  // kaVELm\ �
console.log(decode_and_get_string("5.49147630737933e+23")); // tIZKgNwVtm   // tIZKgNv`B
console.log(decode_and_get_string("3.467299967374622e+23")); // IlERBwnlNL  // IlERBwp�^
console.log(decode_and_get_string("3.837378487483749e+23")); // QBxpRcezrb  // QBxpRce��
console.log(decode_and_get_string("4.647527782090808e+23")); // bjLpghbwJg  // bjLpghe�8
*/
