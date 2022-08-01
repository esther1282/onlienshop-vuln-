var originalAlert = window.alert;
function copyToClipboard(text) {
    window.prompt("축하합니다 ! flag 획득 ! \n\nCopy to clipboard: Ctrl+C, Enter", text);
}
window.alert = function(s) {
  parent.postMessage("success", "*");
  var message = "GOTROOT{y0oure_Xss_m@st3r}"
  setTimeout(function() {
    copyToClipboard(message);
  }, 50);
}