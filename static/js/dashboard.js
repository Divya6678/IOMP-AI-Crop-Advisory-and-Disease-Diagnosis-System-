function runAI() {

  const fileInput = document.querySelector("input[type='file']");
  const cropSelect = document.getElementById("cropSelect");
  const result = document.getElementById("result");
  const advisory = document.getElementById("advisory");

  if (!cropSelect.value) {
    alert("Please select your plant/crop type before running the diagnosis.");
    return;
  }

  if (!fileInput.files.length) {
    alert("Please upload a leaf image before running diagnosis.");
    return;
  }

  result.innerHTML = "⏳ Running AI diagnosis...";
  advisory.innerHTML = "Waiting for AI advisory...";

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("crop", cropSelect.value);

  fetch("/predict", {
    method: "POST",
    body: formData
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Server error");
      }
      return response.json();
    })
    .then(data => {

      if (data.error) {
        result.innerHTML = "❌ " + data.error;
        advisory.innerHTML = "Please upload a valid JPG or PNG leaf image.";
        return;
      }

      displayResult(data);
    })
    .catch(error => {
      result.innerHTML = "❌ Server connection failed.";
      advisory.innerHTML = "Make sure Flask server is running.";
      console.error(error);
    });
}


/* ==============================
   DISPLAY RESULT FUNCTION
============================== */

function displayResult(data) {

  const result = document.getElementById("result");
  const advisory = document.getElementById("advisory");

  result.innerHTML = `
    <strong>Result:</strong> ${data.disease}<br><br>
    <strong>Disease Severity:</strong><span class="badge ${data.severity.toLowerCase()}">
      ${data.severity.toUpperCase()}
    </span><br><br>
    <strong>Disease Confidence:</strong> ${data.confidence}%
  `;

  advisory.innerHTML = `
    🌱 <strong>Organic:</strong> ${data.organic}<br><br>
    🧪 <strong>Chemical:</strong> ${data.chemical}<br><br>
    🚫 <strong>Prevention:</strong> ${data.prevention}
  `;
}