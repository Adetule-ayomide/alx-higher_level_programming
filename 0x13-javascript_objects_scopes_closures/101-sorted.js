#!/usr/bin/node

const { dict } = require('./101-data');

const userOccurrence = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (!userOccurrence[occurrence]) {
    userOccurrence[occurrence] = [];
  }

  userOccurrence[occurrence].push(userId);
}

console.log(userOccurrence);
