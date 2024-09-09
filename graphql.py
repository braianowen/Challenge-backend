from flask import Flask
from flask_graphql import GraphQLView
import graphene
import pandas as pd

# Cargar el CSV usando pandas
df = pd.read_csv('data.csv')

class Product(graphene.ObjectType):
    id_tie_fecha_valor = graphene.String()
    id_cli_cliente = graphene.String()
    desc_ga_nombre_producto = graphene.String()
    desc_ga_categoria_producto = graphene.String()
    fc_producto_cant = graphene.Int()

class Query(graphene.ObjectType):
    products = graphene.List(Product)

    def resolve_products(self, info):
        # Convertir DataFrame a lista de objetos Product
        products = []
        for _, row in df.iterrows():
            product = Product(
                id_tie_fecha_valor=row['id_tie_fecha_valor'],
                id_cli_cliente=row['id_cli_cliente'],
                desc_ga_nombre_producto=row['desc_ga_nombre_producto'],
                desc_ga_categoria_producto=row['desc_ga_categoria_producto'],
                fc_producto_cant=row['fc_producto_cant'],
            )
            products.append(product)
        return products

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Para activar la interfaz de GraphiQL
    )
)

if __name__ == '__main__':
    app.run(debug=True)
