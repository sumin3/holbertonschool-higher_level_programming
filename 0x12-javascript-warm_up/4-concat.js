#!/usr/bin/node
/* prints the first argument passed to it */
if (!process.argv[2] && !process.argv[3]) {
  console.log('undefined is undefined');
} else if (process.argv[2] && !process.argv[3]) {
  console.log(process.argv[2], 'is undefined');
} else if (process.argv[2] && process.argv[3]) {
  console.log(process.argv[2], 'is', process.argv[3]);
}
