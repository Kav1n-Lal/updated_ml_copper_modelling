import streamlit as st  
import datetime
import pandas as pd
import pickle
from datetime import datetime as dt
z=pd.read_csv('Cu_regressor_features.csv')

s=st.sidebar.selectbox('Choose one',['Copper price prediction','Status prediction'])

if s=='Copper price prediction':
    def load_model():
        with open('rev_saved_steps_regressor.pkl','rb') as file:
            data=pickle.load(file)
        return data

    data=load_model()

    regressor=data['model']
    mean_enc=data['mean_enc']
    ordinal_enc=data['ordinal_enc']
    
    st.title("COPPER SELLING PRICE PREDICTION")
    st.write("""### We need some information to predict selling price""")

    # Storing all user input 
    input_dict={'item_date':'','customer':'','status':'','application':'','thickness':'',
                'width':'','material_ref':'','product_ref':'','delivery date':''}

    form = st.form("form1")
    
    d1=form.date_input('Please select copper stock purchase date',
                     min_value=datetime.date(2019, 1, 1),max_value=datetime.datetime.now())
    
    cstmr=form.selectbox('Choose customerID',list(z['customer'].apply(lambda x:round(float(x))).sort_values().unique()))
    input_dict['customer']=str(cstmr)+'.0'

    sts=form.selectbox('Choose Status',list(z['status'].unique()))
    input_dict['status']=sts 

    app=form.selectbox('Choose applicationID',list(z['application'].unique()))
    input_dict['application']=str(app)

    thick=form.selectbox('Choose thickness',list(z['thickness'].apply(lambda x:(float(x))).sort_values().unique()))
    input_dict['thickness']=str(thick)

    wid=form.selectbox('Choose width size',list(z['width'].apply(lambda x:(float(x))).sort_values().unique()))   
    input_dict['width']=str(wid)    

    mat=form.selectbox('Choose material_ref',list(z['material_ref'].unique()))
    input_dict['material_ref']=str(mat)

    pro=form.selectbox('Choose product_ref',list(z['product_ref'].unique()))
    input_dict['product_ref']=str(pro)

    d2=form.date_input('Please select on which day you are planning to sell the copper stock',
                     min_value=datetime.datetime.now(),max_value=datetime.date(2024, 12, 31)) 
    
    ok=form.form_submit_button("PREDICT") #   
    if ok:
        v=[]
        v2=[]
        
        purchase_date = dt.strptime(str(d1), "%Y-%m-%d")
        selling_date = dt.strptime(str(d2), "%Y-%m-%d")
        if purchase_date.date() >= selling_date.date():
            st.warning('### Your purchase_date and selling date are same!' )
        else:
            p=str(purchase_date).split('-')
            purchase_date=''.join(p)
            v.append(purchase_date[4:8])
            v.append('.0')
            input_dict['item_date']=''.join(v) 
            
            p1=str(selling_date).split('-')
            selling_date=''.join(p1)
            v2.append(selling_date[4:8])
            v2.append('.0')
            input_dict['delivery date']=''.join(v2)
            
            A=pd.DataFrame(input_dict,index=[1])
            A=mean_enc.transform(A)
            A=ordinal_enc.transform(A)
            y_pred=regressor.predict(A)
            u=str(round(y_pred[0],2))+'/-'
            st.write(f'### Predicted Copper Selling Price is : {u}')
        
else:
    z=pd.read_csv('Cu_classifier_features.csv')
    def load_model():
        with open('rev_saved_steps_classifier.pkl','rb') as file:
            data=pickle.load(file)
        return data

    data=load_model()

    classifier=data['model']
    mean_enc=data['mean_enc']
    scaler=data['scaler']
    
    #def show_predict_page():
    st.title("COPPER STATUS PREDICTION")
    st.write("""### We need some information to predict status""")

    # Storing all user input 
    input_dict={'item_date':'','country':'','item type':'','customer':'',
                'application':'','width':'','material_ref':'','product_ref':'',
                'delivery date':'','selling_price':''}

    form = st.form("form1")
    d1=form.date_input('When did the customer bought the copper stock',
                     min_value=datetime.date(2019, 1, 1),max_value=datetime.datetime.now())

    cnty=form.selectbox('Choose country',list(z['country'].unique()))
    input_dict['country']=str(cnty)   

    ity=form.selectbox('Choose item_type',list(z['item type'].unique()))
    input_dict['item type']=str(ity)

    cstmr=form.selectbox('Choose customerID',list(z['customer'].apply(lambda x:round(float(x))).sort_values().unique()))
    input_dict['customer']=str(cstmr)+'.0'

    app=form.selectbox('Choose applicationID',list(z['application'].unique()))
    input_dict['application']=str(app)

    wid=form.selectbox('Choose width size',list(z['width'].apply(lambda x:(float(x))).sort_values().unique()))   
    input_dict['width']=str(wid)    

    mat=form.selectbox('Choose material_ref',list(z['material_ref'].unique()))
    input_dict['material_ref']=str(mat)

    pro=form.selectbox('Choose product_ref',list(z['product_ref'].unique()))
    input_dict['product_ref']=str(pro)
 
    sell=form.slider('Choose selling price',min_value=-1160,max_value=6000)
    input_dict['selling_price']=str(sell)
            
    d2=form.date_input('When did the customer sold the copper stock',
                     min_value=datetime.datetime.now(),max_value=datetime.date(2024, 12, 31))

    ok=form.form_submit_button("PREDICT") #   
    if ok:
        v=[]
        v2=[]
        
        purchase_date = dt.strptime(str(d1), "%Y-%m-%d")
        selling_date = dt.strptime(str(d2), "%Y-%m-%d")
        if purchase_date.date() >= selling_date.date():
            st.warning('### Your purchase_date and selling date are same!' )
        else:
            p=str(purchase_date).split('-')
            purchase_date=''.join(p)
            v.append(purchase_date[4:8])
            v.append('.0')
            input_dict['item_date']=''.join(v) 
            
            p1=str(selling_date).split('-')
            selling_date=''.join(p1)
            v2.append(selling_date[4:8])
            v2.append('.0')
            input_dict['delivery date']=''.join(v2)
            
            #st.write(input_dict)
            
            A=pd.DataFrame(input_dict,index=[1])
            A=mean_enc.transform(A)
            A=scaler.transform(A)
            y_pred=classifier.predict(A)
            u=(y_pred[0])
            if u==1:
                st.success('### Predicted Customer lead status : "WON"') 
            else:        
                st.error('### Predicted Customer lead status : "LOST"')