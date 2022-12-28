# SISTEMA DE VENTA DE PULSERAS| PyV | juanigomez - pynet

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

navBar = option_menu(

    menu_title = None,
    options = ["Database", "Purchase", "Sales"],
    icons = ["folder2", "cart3","database-check"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal"

)

def get_Data(filename):
    data = pd.read_csv(filename)
    return data

def get_Index(value, all_Values):

    index = 0
    count = int(len(all_Values) - 1)

    if value != all_Values[index]:
        for n in all_Values:
            while value != all_Values[index]:
                if index == count:
                    break
                else:
                    index += 1

    return index


def Database():

    def Decorations():

        header = st.container()
        inputs = st.container()
        button = st.container()
        table = st.container()

        with header:

            st.header("Info. Decoraciones: ")
            st.text("Accede e ingresa decoraciones...")

        with inputs:

            Name = st.text_input("Nombre de la decoracion: ")
            Amount = st.select_slider("Cantidad", ['poca', 'suficiente', 'mucha'])

        with button:

            decorations_Dataset = get_Data('decorations.csv')
            all_Decorations = list(decorations_Dataset.iloc[:,0])
            index = get_Index(Name, all_Decorations)

            input_decoration_btn = st.button("Guardar")
            if input_decoration_btn:

                if Name == all_Decorations[index]:

                    current_Decoration = Name
                    st.error(f"Ya existe ese item...({index})")

                else:

                    new_data = [[Name, Amount]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('decorations.csv', mode='a', index=False, header=False)

                    current_Decoration = Name
                    st.error(f"Nueva decoracion: {current_Decoration}")

        with table:

            st.subheader("Decoraciones: ")
            st.text("Tabla con todas las decoraciones: ")

            decorations_Table = get_Data('decorations.csv')
            st.table(decorations_Table)

    def Materials():

        header = st.container()
        inputs = st.container()
        button = st.container()
        table = st.container()

        with header:

            st.header("Info. Materiales")
            st.text("Accede e ingresa materiales...")

        with inputs:

            Name = st.text_input("Nombre del Material: ")
            Amount = st.select_slider("Cantidad", ['poca', 'suficiente', 'mucha'])

        with button:

            materials_Dataset = get_Data('materials.csv')
            all_Materials = list(materials_Dataset.iloc[:,0])
            index = get_Index(Name, all_Materials)

            input_material_btn = st.button("Guardar")
            if input_material_btn:

                if Name == all_Materials[index]:

                    current_Material = Name
                    st.error(f"Ya existe ese item...({index})")

                else: 

                    new_data = [[Name, Amount]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('materials.csv', mode='a', index=False, header=False)

                    current_Material = Name
                    st.error(f"Nuevo material: {current_Material}")

        with table:

            st.subheader("Materiales: ")
            st.text("Tabla con todos los materiales: ")

            materials_Table = get_Data('materials.csv')
            st.table(materials_Table)

    def Products():

        header = st.container()
        inputs = st.container()
        button = st.container()
        table = st.container()

        with header:

            st.header("Info. Productos: ")
            st.text("Accede e ingresa productos...")

        with inputs:

            col1, col2, col3 = st.columns(3)

            with col1:

                Name = str(st.text_input("Nombre del producto: "))
                Stock = st.slider("Cantidad", 1, 10)

                materials_Dataset = get_Data('materials.csv')
                all_Materials = list(materials_Dataset.iloc[:,0])
                mat = st.selectbox("Selecciona el material principal: ", all_Materials)

                decorations_Dataset = get_Data('decorations.csv')
                all_Decorations = list(decorations_Dataset.iloc[:,0])
                dec = st.multiselect("Selecciona las decoraciones: ", all_Decorations)

            with col2:

                if mat == "CUENCAS":

                    color = st.multiselect("Selecciona el color: ", ['BLANCO', 'NEGRO'], max_selections = 2)

                elif mat == "HILO ENCERADO":

                    color = st.selectbox("Selecciona el color: ", ['VERDE MARINO', 'VERDE CLARO', 'MARRON', 'OTRO'])
                
                elif mat == "CUERINA":

                    color1 = st.selectbox("Primer color: ", ['beige', 'celeste', 'violeta', 'bordo'])
                    color2 = st.selectbox("Segundo color: ", ['beige', 'celeste', 'violeta', 'bordo'])
                    color3 = st.selectbox("Tercer color: ", ['beige', 'celeste', 'violeta', 'bordo'])

                    color = [color1, color2, color3]

            with col3:

                Price = st.slider("Ingresa el precio: ", 1, 500, step = 10)

        with button:

            products_Dataset = get_Data('products.csv')
            all_Products = list(products_Dataset.iloc[:,0])
            index = get_Index(Name, all_Products)

            input_product_btn = st.button("Guardar")
            if input_product_btn:

                if Name == all_Products[index]:

                    current_Product = Name
                    st.error(f"Item ({index}), guardando cambios...")

                    def update_Product_Data():

                        df = get_Data('products.csv') 

                        df.loc[index, 'NOMBRE'] = Name
                        df.loc[index, 'STOCK'] = Stock
                        df.loc[index, 'MATERIAL'] = mat
                        df.loc[index, 'DECORACION'] = dec
                        df.loc[index, 'PRECIO'] = Price
                        
                        df.to_csv('products.csv',index=False)

                    update_Product_Data()

                else:

                    new_data = [[Name, Stock, mat, dec, Price]]
                    df = pd.DataFrame(new_data)
                    df.to_csv('products.csv', mode='a', index=False, header=False)

                    current_Product = Name
                    st.error(f"Nuevo products: {current_Product}")


    all_Pages = {
    "Decoraciones": Decorations,
    "Materiales": Materials,
    "Productos": Products
}
    st.sidebar.title("Sistema: PyV")
    st.sidebar.header("Base de Datos --> ")

    selected_page = st.sidebar.selectbox("Select a page", all_Pages.keys())
    all_Pages[selected_page]()

def Purchase():

    st.header("Purchase page")
    st.warning("In process ...")

def Sales():

    st.header("Sales page")
    st.warning("In process ...")

if navBar == "Database":
    Database()
    
elif navBar == "Purchase":
    Purchase()

elif navBar == "Sales":
    Sales()
