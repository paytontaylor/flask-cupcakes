const $form = $('#form')

$form.on('submit', async (e) => {
    e.preventDefault();

    const $flavor = $('#flavor').val()
    const $size = $('#size').val()
    const $rating = $('#rating').val()
    const $image = $('#image').val()

    const res = await axios.post('/api/cupcakes', {
        flavor: $flavor,
        size: $size,
        rating: $rating,
        image: $image || "https://tinyurl.com/demo-cupcake"
    })

    const $cupcake = $(`<li>${res.data.cupcake.flavor}</li>`)
    const $cupcakes = $('#cupcakes').append($cupcake)
})