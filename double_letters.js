// Create a function that takes a word and returns true if the word has two consecutive identical letters.


function double_letters(word){
    
    for (let i = 0; i < word.length; i++){
        if (word[i] === word[i + 1]) return true;
    }

    return false;
}


console.log(double_letters('  sd aa'));
