fetch("/history-data")
.then(response => response.json())
.then(data => {

  let table = document.getElementById("historyTable");

  data.forEach(item => {
    table.innerHTML += `
      <tr>
        <td>
          <img src="/static/uploads/${item.image || 'default.png'}" alt="Leaf Image" style="width: 60px; height: 60px; border-radius: 6px; object-fit: cover; border: 1px solid var(--card-border);">
        </td>
        <td>${item.disease}</td>
        <td>${item.severity}</td>
        <td>${item.confidence}%</td>
      </tr>
    `;
  });

});