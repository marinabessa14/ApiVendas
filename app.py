from flask import Flask, jsonify, request



app = Flask(__name__)

vendas = [

    {
            'numerovenda': 1,
             'data' : 18/10/2022,
            'cpf_cnpj': '123.123.123-12',
            'nome': 'Jose da Silva',
            'cpf_vendedor': '321.321.321.32',
            'valordeentrada': 5.00,
            'quantidadedeparcela' : 2


    },
    {
        'codproduto': 1,
        'descricao': 'cafe',
        'quantidade': 3,
        'valorunitario': 12.5


    },
    {
        'codproduto': 2,
        'descricao': 'leite',
        'quantidade': 2,
        'valorunitario': 4.75
    



    },

]
@app.route('/venda',methods=['POST'])
def obter_vendas():
    return jsonify(vendas)


@app.route('/venda/1',methods=['GET'])
def obter_vendas_paramentro():
    return jsonify('vendas')

@app.route('/venda/',methods=['GET'])
def obter_vendas_cabecalho():
    return jsonify('numerovenda:1 ', 'data:18/10/2022', 'cpf_cnpj:123.123.123-12','nome:Jose da Silva','cpf_vendedor:321.321.321.32','valortotal 17.75','valordeentrada:5.00','quantidadeparcelas 2')


app.run(port=5000,host='localhost',debug=True)
    
