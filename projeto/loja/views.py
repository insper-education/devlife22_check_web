from django.shortcuts import render
from .models import ItemPedido, Produto, Cliente, Pedido

def index(request):
  all_products = Produto.objects.all()
  return render(request, 'loja/produtos.html', {'produtos': all_products})

def detail_produto(request, produto_id):
  produto = Produto.objects.get(id=produto_id)
  return render(request, 'loja/detalhe_produto.html', {'produto': produto})

def add_pedido(request):
  return render(request, 'loja/pedido.html')

def add_item(request):
  all_products = Produto.objects.all()
  all_clientes = Cliente.objects.all()
  if request.method == 'GET':
    return render(request, 'loja/pedido.html', {'produtos': all_products, 'clientes': all_clientes, 'pedido': ''})  
  elif request.method == 'POST':
    produto_id = request.POST['produto']
    quantidade = request.POST['quantidade']
    if request.POST.get('pedido','') == '':
      cliente_id = request.POST['solicitante']
      cliente = Cliente.objects.get(pk=cliente_id)
      pedido = Pedido(cliente=cliente, valor_total=0, pago=False)
      pedido.save()
    else:
      pedido = Pedido.objects.get(pk=request.POST['pedido'])
      cliente = Cliente.objects.get(pk=request.POST['solicitante'])
    
    item = ItemPedido(produto = Produto.objects.get(pk=produto_id), pedido = pedido, quantidade = quantidade)
    item.save()
    return render(request, 'loja/pedido.html', {'produtos': all_products, 
      'cliente': cliente, 'pedido': pedido.id, 'itens': ItemPedido.objects.filter(pedido=pedido)})
    
def clientes(request):
  #TODO
  pass 

def detail_cliente(request, cliente_id):
  #TODO
  pass

def add_produto(request):
  try:
    p = Produto.objects.create(
      nome = request.POST['nome'], 
      descricao = request.POST['descricao'], 
      preco = request.POST['preco'])
    p.save()
    return render(request, 'loja/detalhe_produto.html', {'produto': p})
  except:
    return render(request, "loja/add_produto.html")

