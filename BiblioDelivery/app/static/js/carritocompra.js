const cards = document.getElementById('cards')
const items = document.getElementById('items')
const footer = document.getElementById('footer')
const fragment = document.createDocumentFragment()
const templateFooter = document.getElementById('template-footer').content
const templateCarrito = document.getElementById('template-carrito').content
let carrito = {}

document.addEventListener('DOMContentLoaded', () =>{
    fetchData()
    if(localStorage.getItem('carrito')){
        carrito = JSON.parse(localStorage.getItem('carrito'))
        pintarCarrito()
    }
})

items.addEventListener('click', e => {
    
    btnAccion(e)
})
const fetchData = async () => {
    try {
        const res = await fetch('/api/lista_productos')
        const data = await res.json()
    } catch (error) {
        console.log(error)
    }
}

const setCarrito = objeto => {
    //console.log(objeto)
    const producto ={
        id: objeto.querySelector('.btn-success').dataset.id,
        title: objeto.querySelector('h5').textContent,
        precio: objeto.querySelector('p').textContent,
        cantidad: 1
    }
    if(carrito.hasOwnProperty(producto.id)){
        producto.cantidad = carrito[producto.id].cantidad+1
    }
    
    carrito[producto.id] = { ...producto }
    pintarCarrito()
}

const pintarCarrito = () => {
    //console.log(carrito)
    items.innerHTML= ''
    Object.values(carrito).forEach(producto => {
        templateCarrito.querySelector('th').textContent = producto.id
        templateCarrito.querySelectorAll('td')[0].textContent = producto.title
        templateCarrito.querySelectorAll('td')[1].textContent = producto.cantidad
        templateCarrito.querySelector('.btn-info').dataset.id = producto.id
        templateCarrito.querySelector('.btn-danger').dataset.id = producto.id
        templateCarrito.querySelector('span').textContent = producto.cantidad * producto.precio

        const clone = templateCarrito.cloneNode(true)
        fragment.appendChild(clone)
    })
    items.appendChild(fragment)


    pintarFooter()

    localStorage.setItem('carrito', JSON.stringify(carrito))
}

const pintarFooter = () =>{
    footer.innerHTML = ''
    if(Object.keys(carrito).length === 0){
        footer.innerHTML = '<th scope="row" colspan="5">Carrito vacío - comience a comprar!</th>'
        return
    } 
    const nCantidad = Object.values(carrito).reduce((acc, {cantidad}) =>acc + cantidad ,0 )
    const nPrecio = Object.values(carrito).reduce((acc, {cantidad,precio}) => acc + cantidad*precio,0)
    
    templateFooter.querySelectorAll('td')[0].textContent = nCantidad
    templateFooter.querySelector('span').textContent = nPrecio

    const clone = templateFooter.cloneNode(true)
    fragment.appendChild(clone)
    footer.appendChild(fragment)

    const btnVaciar = document.getElementById('vaciar-carrito')
    btnVaciar.addEventListener('click',() => {
        carrito = {}
        pintarCarrito()
    })
}

const btnAccion = e => {
    //console.log(e.target)
    //AUMENTAR
    if(e.target.classList.contains('btn-info')){
        console.log(carrito[e.target.dataset.id])
        const producto = carrito[e.target.dataset.id]
        producto.cantidad++
        carrito[e.target.dataset.id] = {...producto}
        pintarCarrito()
    }
    
    if(e.target.classList.contains('btn-danger')){
        const producto = carrito[e.target.dataset.id]
        producto.cantidad--
        if(producto.cantidad === 0){
            delete carrito[e.target.dataset.id]
        }
        pintarCarrito()
    }
    e.stopPropagation()
}
