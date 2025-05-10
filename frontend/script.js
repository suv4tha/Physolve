document.getElementById('physicsForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const velocity = document.getElementById('velocity').value;
    const angle = document.getElementById('angle').value;
  
    const res = await fetch('http://127.0.0.1:5000/projectile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ velocity, angle })
    });
  
    const data = await res.json();
    document.getElementById('result').innerHTML =
      `<p>Max Height: ${data.max_height.toFixed(2)} m</p>
       <p>Range: ${data.range.toFixed(2)} m</p>`;
  });
  