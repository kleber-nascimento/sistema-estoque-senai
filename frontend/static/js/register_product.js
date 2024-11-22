const form = document.getElementById('product-form');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const productData = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        price: parseFloat(document.getElementById('price').value),
        quantity: parseInt(document.getElementById('quantity').value, 10)
    };

    try {
        const response = await fetch('http://127.0.0.1:5001/api/products', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(productData)
        });

        if (response.ok) {
            alert('Produto cadastrado com sucesso!');
            form.reset(); // Limpar o formulário
        } else {
            const errorData = await response.json();
            alert(`Erro ao cadastrar produto: ${errorData.message}`);
        }
    } catch (error) {
        alert('Erro de conexão com o servidor.');
        console.error(error);
    }
});
