#!/usr/bin/node

const fs = require('fs');

const contentFile = process.argv[2];
const content = process.argv[3];

fs.writeFile(contentFile, content, 'utf-8', err  => {
	if (err) {
		console.error(err);
		return;
	}
});
