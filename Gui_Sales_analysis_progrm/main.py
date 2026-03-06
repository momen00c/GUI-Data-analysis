from src.loader import *
from src.cleaner import clean_data,drop_column
from src.analyzer import *
from src.feature_engineering import add_data_feature_eng
from src.searcher import search
from src.exporter import expoert_excl
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk

global df
df = None

def set_data():
    global df
    file_path = filedialog.askopenfilename(defaultextension=r'\data',title="select file", filetypes=[("CSV files", "*.csv")
                                                                    , ("Excel files", "*.xlsx")])
    if search(file_path) =='csv':
            df=load_csv_data(file_path)
    else:

        df=load_excl_data(file_path)


def delet_col():
    global df
    if df is None:
        messagebox.showerror(title="erorr",detail="plese select data first")
    else:
        se_top = Toplevel(root)    
        options = preview_columns(df)
        del_box=ttk.Combobox(se_top,values=options)
        del_box.grid(row=0,column=1,pady=5,padx=5)
        del_col = Button(se_top, text="Delet",command=lambda:drop_column(df,del_box.get(),se_top))
        del_col.grid(row=1,column=1)
        return df

def select():
   # global  df 
    global Top
    global mainframe
    if df is None:
        messagebox.showerror(detail="plese select data first")
        pass
    else:
        Top = Toplevel()
        Top.geometry('500x700')
        Top.configure(background="#9CBDDA")
        mainframe = Frame(Top)
        mainframe.grid(row=0,column=0)

        options = preview_columns(df)
        invoice_id = Label(mainframe,text='invoice_id')
        invoice_id.grid(row=0,column=0)
        invoice_id_box=ttk.Combobox(mainframe,values=options)
        invoice_id_box.grid(row=0,column=1,pady=5)

        branch = Label(mainframe,text='branch')
        branch.grid(row=1,column=0)
        branch_box=ttk.Combobox(mainframe,values=options)
        branch_box.grid(row=1,column=1,pady=5)

        city = Label(mainframe,text='city')
        city.grid(row=2,column=0)
        city_box=ttk.Combobox(mainframe,values=options)
        city_box.grid(row=2,column=1,pady=5)

        customer_type = Label(mainframe,text='customer_type')
        customer_type.grid(row=3,column=0)
        customer_type_box=ttk.Combobox(mainframe,values=options)
        customer_type_box.grid(row=3,column=1,pady=5)

        gender = Label(mainframe,text='gender')
        gender.grid(row=4,column=0)
        gender_box=ttk.Combobox(mainframe,values=options)
        gender_box.grid(row=4,column=1,pady=5)

        product_line = Label(mainframe,text='product_line')
        product_line.grid(row=5,column=0)
        product_line_box=ttk.Combobox(mainframe,values=options)
        product_line_box.grid(row=5,column=1,pady=5)

        unit_price = Label(mainframe,text='unit_price')
        unit_price.grid(row=6,column=0)
        unit_price_box=ttk.Combobox(mainframe,values=options)
        unit_price_box.grid(row=6,column=1,pady=5)

        quantity = Label(mainframe,text='quantity')
        quantity.grid(row=7,column=0)
        quantity_box=ttk.Combobox(mainframe,values=options)
        quantity_box.grid(row=7,column=1,pady=5)
        
        total = Label(mainframe,text='total')
        total.grid(row=8,column=0)
        total_box=ttk.Combobox(mainframe,values=options)
        total_box.grid(row=8,column=1,pady=5)

        date = Label(mainframe,text='date')
        date.grid(row=9,column=0)
        date_box=ttk.Combobox(mainframe,values=options)
        date_box.grid(row=9,column=1,pady=5)

        time = Label(mainframe,text='time')
        time.grid(row=10,column=0)
        time_box=ttk.Combobox(mainframe,values=options)
        time_box.grid(row=10,column=1,pady=5)

        payment_type = Label(mainframe,text='payment_type')
        payment_type.grid(row=11,column=0)
        payment_type_box=ttk.Combobox(mainframe,values=options)
        payment_type_box.grid(row=11,column=1,pady=5)

        cogs = Label(mainframe,text='cogs')
        cogs.grid(row=12,column=0)
        cogs_box=ttk.Combobox(mainframe,values=options)
        cogs_box.grid(row=12,column=1,pady=5)

        gross_margin = Label(mainframe,text='gross_margin')
        gross_margin.grid(row=13,column=0)
        gross_margin_box=ttk.Combobox(mainframe,values=options)
        gross_margin_box.grid(row=13,column=1,pady=5)

        gross_income = Label(mainframe,text='gross_income')
        gross_income.grid(row=14,column=0)
        gross_income_box=ttk.Combobox(mainframe,values=options)
        gross_income_box.grid(row=14,column=1,pady=5)

        rating = Label(mainframe,text='rating')
        rating.grid(row=15,column=0)
        rating_box=ttk.Combobox(mainframe,values=options)
        rating_box.grid(row=15,column=1,pady=5)

        def mapper():
            global df
            mapping = {
            invoice_id_box.get(): "invoice_id",
            branch_box.get(): "branch",
            city_box.get(): "city",
            customer_type_box.get(): "customer_type",
            gender_box.get(): "gender",
            product_line_box.get(): "product_line",
            unit_price_box.get(): "unit_price",
            quantity_box.get(): "quantity",
            total_box.get(): "total",
            date_box.get(): "date",
            time_box.get(): "time",
            payment_type_box.get(): "payment_type",
            cogs_box.get(): "cogs",
            gross_margin_box.get(): "gross_margin",
            gross_income_box.get(): "gross_income",
            rating_box.get(): "rating",
                          }
            print(mapping)
            mapping = {k:v for k,v in mapping.items() if v!=''}
            df.rename(columns=mapping,inplace=True)
            print(preview_columns(df))

            if not mapping:
                messagebox.showwarning("Warning", "Please map at least one column")
                return df
            else:
                print(df.columns.tolist())
                
            return df 
        ed_frame = Frame(Top)
        ed_frame.place(x=300,y=100)
        delet=Button(ed_frame,text="Feature engeering",command=lambda:add_data_feature_eng(df),font=("Arial", 9, "bold"),bg='#2E9AF9',width=20,height=3,)
        delet.grid(row=14,column=5,padx=10,pady=10) 
        apply=Button(ed_frame,text="Apply",command=mapper,font=("Arial", 9, "bold"),bg='#2E9AF9',width=20,height=3,)
        apply.grid(row=15,column=5,padx=10,pady=10)
        ok_slect=Button(ed_frame,text="Done",command=Top.destroy,font=("Arial", 9, "bold"),bg='#2E9AF9',width=20,height=3,)
        ok_slect.grid(row=17,column=5,padx=10,pady=10)
        add_defult=Button(ed_frame,text="Add Defult",command=lambda:setting_data(df),font=("Arial", 9, "bold"),bg='#2E9AF9',width=20,height=3,)
        add_defult.grid(row=18,column=5,padx=10,pady=10)        
        #return df 

def start_clean_and_fet():
    global df
    if df is None:
        messagebox.showerror(detail="plese select data first")
    else:
        df=clean_data(df)
        #fetu_eng
        df=add_data_feature_eng(df)
        return df

#analyze


# tree views
def show_preview():
    global df
    if df is None:
        messagebox.showerror(detail="Plese select data first")
    else:
        wind = Toplevel()
        wind.title('Data Preview')
        scroller =ttk.Scrollbar(wind,orient='vertical')
        scroller.pack(side='right',fill='y')
        tree  = ttk.Treeview(wind,yscrollcommand=scroller.set)
        scroller.config(command=tree.yview)
        tree.pack(fill='both', expand=True)
        tree['columns'] = list(df.columns)
        tree['show']= 'headings'

        for col in df.columns:
            tree.heading(col,text=col)
            tree.column(col,width=50)
        for _,row in df.iterrows():
            tree.insert('','end',values=list(row))
        #Button(text='Close',command=wind.destroy).pack(pady=5)



def show_kpis(df,analysis_box):
    kpis = calc_kpis(df)
    text= '------------KPIS----------\n'
    text += f'Total Sales : {kpis['total_sales']:.2f}\n'
    text += f'Average Rating : {kpis['avg_rating']:.2f}\n'
    text += f'Total Quantity : {kpis['total_quantity_sold']:.2f}\n'
    text += f'Total Revenue : {kpis['total_revenue']:.2f}\n'
    text += f'Total orders : {len(df):.2f}\n'
    analysis_box.delete('1.0',END)
    analysis_box.insert(END,text)

def show_sales(df,analysis_box):
    sales = sales_eda(df)
    text= '------------Sales----------\n'
    text += f'Sales By Day :\n{sales['sales_by_day'].to_string()}\n\n'
    text += f'Sales By Bayment Type :\n{sales['sales_by_payment_type'].to_string()}\n\n'
    text += f'Sales By product line :\n{sales['sales_by_product_line'].to_string()}\n\n'
    text += f'Sales By City :\n{sales['sales_by_city'].to_string()}\n\n'
    analysis_box.delete('1.0',END)
    analysis_box.insert(END,text)

def show_customer(df,analysis_box):
    sales = customer_eda(df)
    text= '------------Cusomer----------\n'
    text += f'Aerage Rating By Customer Type :\n{sales['avg_rating_by_customer_type'].to_string()}\n\n'
    text += f'Sales By Customer Type :\n{sales['sales_by_customer_type'].to_string()}\n\n'
    text += f'Count By Gender :\n{sales['count_by_gender'].to_string()}\n\n'
    analysis_box.delete('1.0',END)
    analysis_box.insert(END,text)

def show_product(df,analysis_box):
    sales = product_eda(df)
    text= '------------Products----------\n'
    text += f'Aerage Unit Price By Product :\n{sales['avg_unit_price_by_product'].to_string()}\n\n'
    text += f'Count Product By Category :\n{sales['count_product_by_category'].to_string()}\n\n'
    text += f'Quantity Sold By Product :\n{sales['quantity_sold_by_product'].to_string()}\n\n'

    analysis_box.delete('1.0',END)
    analysis_box.insert(END,text)


def analysis(df):
    if df is None:
        messagebox.showerror(detail="plese select data first")
    else:
        rop = Toplevel()
        rop.geometry('800x800')


        frame_text = Frame(rop)
        frame_text.grid(row=0,column= 0 ,pady=30)

        frame_button = Frame(rop)
        frame_button.place(x=600,y=100)
        scllor =ttk.Scrollbar(frame_text,orient='vertical')
        scllor.grid(row=0,column=5,sticky='ns')

        analysis_box = Text(frame_text,width=70,height=40,padx=5,font=("Arial",11, "bold"),bg="#ABCEEC",yscrollcommand=scllor.set)
        analysis_box.grid(row=0,column= 0,padx=5 )
        scllor.config(command=analysis_box.yview)
        

        EDAs = Button(frame_button,text='KPIS',font=("Arial", 10, "bold"),bg='#2E9AF9',width=20,height=3,command=lambda:show_kpis(df,analysis_box))
        EDAs.grid(row=0,column=1,padx=5,pady=8) 
        EDAs = Button(frame_button,text='Sales EDA',font=("Arial", 10, "bold"),bg='#2E9AF9',width=20,height=3,command=lambda:show_sales(df,analysis_box))
        EDAs.grid(row=1,column=1,padx=5,pady=8) 
        EDAs = Button(frame_button,text='Customer EDA',font=("Arial", 10, "bold"),bg='#2E9AF9',width=20,height=3,command=lambda:show_customer(df,analysis_box))
        EDAs.grid(row=2,column=1,padx=5,pady=8) 
        EDAs = Button(frame_button,text='Products EDA',font=("Arial", 10, "bold"),bg='#2E9AF9',width=20,height=3,command=lambda:show_product(df,analysis_box))
        EDAs.grid(row=3,column=1,padx=5,pady=8) 





root = tk.Tk()
root.configure(bg="#89C2F4")
root.geometry('900x800')
img = Image.open('er.jpg')
img = img.resize((700,700))
bg_image = ImageTk.PhotoImage(img)
bs=Label(root,image=bg_image)
bs.place(x=0,y=0)

buttons_frame = Frame(root,bg="#95C2E9")
buttons_frame.place(relx=.4,rely=0.93,anchor='center')
# buttons
set_df=Button(buttons_frame,text="Set Data",font=("Arial", 10, "bold"),bg='#2E9AF9',command=set_data,width=20,height=3,)
set_df.grid(row=1,column=0,padx=5,pady=5) 

analy=Button(buttons_frame,text="Analysis",font=("Arial",10, "bold"),bg='#2E9AF9',command=lambda:analysis(df),width=20,height=3,)
analy.grid(row=1,column=3,padx=5,pady=5) 

select_col=Button(buttons_frame,text="edit columns",font=("Arial", 10, "bold"),bg='#2E9AF9',command=select,width=20,height=3)
select_col.grid(row=1,column=1,padx=5,pady=5) 

delet=Button(buttons_frame,text="Remove column",font=("Arial", 10, "bold"),bg='#2E9AF9',command=delet_col,width=20,height=3,)
delet.grid(row=1,column=2,padx=5,pady=5,sticky='s') 

bar_frame = Frame(root,bg="#95C2E9")
bar_frame.place(x=800,y=150,anchor='center')

show_pre=Button(bar_frame,text="Show Preview",font=("Arial", 10, "bold"),anchor='center',bg='#2E9AF9',command=show_preview,width=19,height=3,)
show_pre.grid(row=3,column=5,padx=5,pady=8) 
export=Button(bar_frame,text="Export to excl ",font=("Arial", 10, "bold"),anchor='center',bg='#2E9AF9',command=lambda:expoert_excl(df),width=19,height=3,)
export.grid(row=4,column=5,padx=5,pady=8) 
dashboard=Button(bar_frame,text="Dashboard ",font=("Arial", 10, "bold"),anchor='center',bg='#2E9AF9',command=open_power_pi,width=19,height=3,)
dashboard.grid(row=5,column=5,padx=5,pady=8) 

root.mainloop()
