#!/usr/bin/node

exports.esrever = function (list) {
  const listlen = list.length - 1;
  const newList = [];
  for (let i = listlen; i >= 0; i--) {
    newList.push(list[i]);
  }
  return (newList);
};
