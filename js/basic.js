    function profileVisible(id) {
  document.getElementById("tblNames").style.display = "none";
  document.getElementById("navHide").style.display = "none";
  document.getElementById("page2").style.display= "inline";
}
var rawTemplate = '<p>Hello {{name}}</p>'; // (step 1)

var compiledTemplate = Handlebars.compile(rawTemplate); // (step 2)

var html = compiledTemplate({ name : 'World' }); // (step 3)

// html content will now be: <p>Hello World</p>
