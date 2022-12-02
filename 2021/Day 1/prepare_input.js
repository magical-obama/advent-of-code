const fs = require('fs');

var input_file = String(fs.readFileSync('input.txt'));
var input_list = input_file.split('\n');
// console.log(input_list);

var output = [];
const letters = Array.from('ABCDEFGHIJKLMNOPQRSTUVWXYZ');

function getLettersForIndex(index) {
    let output_string = "";
    output_string += letters[index];
    if (letters[index - 1] != undefined) {
        output_string += letters[index - 1];
    }
    if (letters[index - 2] != undefined) {
        output_string += letters[index - 2];
    }
    output_string = Array.from(output_string).sort().join('');
    return output_string;
}

for (let index = 0; index < input_list.length; index++) {
    const number = input_list[index];
    output.push({key: number, value: getLettersForIndex(index)});
    fs.writeFileSync("prepared_input.txt", JSON.stringify(output));
}