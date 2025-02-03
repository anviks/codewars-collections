/*
 * https://www.codewars.com/kata/527a6e602a7db3456e000a2b
 */


Object.prototype.hash = function(path) {
  return eval('this?.' + path.replaceAll('.', '?.'));
};
