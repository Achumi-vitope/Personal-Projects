// $(function () {
//     $('[data-toggle="tooltip"]').tooltip()
// })

// // Delete the entire text
// function text_delete(){ 
//     let get_text = document.getElementById('generatedContent');
//     get_text.value = "";
// }

// // Convert selected text to upper case
// function upper() {
//     const textarea = document.getElementById('generatedContent');
//     const start = textarea.selectionStart;
//     const end = textarea.selectionEnd;

//     if (start !== end) {
//         const selectedText = textarea.value.substring(start, end);
//         const uppercaseText = selectedText.toUpperCase();
//         textarea.value =
//             textarea.value.substring(0, start) +
//             uppercaseText +
//             textarea.value.substring(end);
//     }
// }

// //Lowecase selected text
// function lower() {
//     const textarea = document.getElementById('generatedContent');
//     const start = textarea.selectionStart;
//     const end = textarea.selectionEnd;

//     if (start !== end) {
//         const selectedText = textarea.value.substring(start, end);
//         const uppercaseText = selectedText.toLowerCase();
//         textarea.value =
//             textarea.value.substring(0, start) +
//             uppercaseText +
//             textarea.value.substring(end);
//     }
// }

var quill = new Quill('#editor', {
    modules: {
      'history': {          // Enable with custom configurations
        'delay': 2500,
        'userOnly': true
      },
      'syntax': true        // Enable with default configuration
    }
  });