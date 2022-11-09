
def bank_stament_read(file_name,bank_name):
    import numpy as np                        # Numerical Python package
    import tabula                             # PDF table extra package
    import pandas as pd
    import os
    import re,string
    import operator as op
    import sys
    from dateutil.parser import parse # Fixing the dates
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")
    
    pdf_file = file_name
    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns',None)
    df = tabula.read_pdf(pdf_file, pages = 'all',multiple_tables=True)
    df_list=df
    col_list=["Description","Narration","Remarks","Particulars","DESCRIPTION","Description","Description","PARTICULARS",
                  "Transaction Details","Narration","NARRATION","PERTICULERS","Details of transaction","ransaction Remarks",
                 "Transaction\rParticulars","Transaction Description","ransaction Remarks","Account Description","NARATION",
                 "Narration Chq/Ref No","Deposits","Amount (Rs.)","Credit","CREDIT","Deposit Amt.","DEPOSIT","Deposit",
          "Deposit Amount\r(INR )","Amount","Deposit Amt","Type","Deposit Balance","WithDrawal","Value",
              "Credit (Rs.)","Withdrawal Amt. Deposit Amt.","Deposit Amount\r(INR )","Credit(Rs)","Withdrawals Deposits",
               "Cr Amount","Withdrawal (Dr)/","Withdrawal Amt.","Withdrawal","Withdrawal","DEBIT","Withdrawals","Debit",
          "Withdrawal (Dr)" ,"Withdrawal Amt. Deposit Amt.","Withdrawal (Dr)/","Withdrawal Amount\r(INR )","Debit (Rs.)",
          "Debit(Rs)","WITHDRAWALS","Withdrawal INR","Withdrawal Amt","Amount","Withdrawal Amount","Withdrawals Deposits",
             "Dr Amount", "Balance","Closing Balance","BALANCE","Running Balance","BALANCE","Balance (INR )","Amount","MODE**",
                "Running","Balance(Rs)","Total Amount\rDr/Cr","Date","date","Transaction","Txn","Transaction Date","Debit/Credit",
          "Transaction date", "Txn Date", "Tran Date","Balance (?)","Branch","Cheque No","Chq./Ref.","Entry Date",'Cheque',
             "TRANSACTION\rDATE","Trans Date","Tran Date","DATE","Post Date","Value\rDate","Date (Value\rDate)","Tran Date",
             "Txn dt", "Txn Dt","Value Date" ,'Chq./Ref.No.','Value Dt',"Chq\rNo.","Transaction Description","Total Amount\rDr/Cr",
          "Debit (Rs.)","Credit (Rs.)","Balance (Rs.)","Dr Amount","Cr Amount","Instruments","Total Amou"]

    date_list = ["Date","date","Transaction","Txn","Transaction Date","Transaction date", "Txn Date", "Tran Date","Date",
             "TRANSACTION\rDATE","Trans Date","Tran Date","DATE","Post Date","Value\rDate","Date (Value\rDate)",
             "Txn dt", "Txn Dt","Value Date"]
    
    narration_list = ["Description","Narration","Remarks","Particulars","DESCRIPTION","Description","Description","PARTICULARS",
                  "Transaction Details","Narration","NARRATION","PERTICULERS","Details of transaction","ransaction Remarks",
                 "Transaction\rParticulars","Transaction Description","ransaction Remarks","Account Description","NARATION",
                 "Narration Chq/Ref No"]

    credit_list = ["Deposits","Amount (Rs.)","Credit","CREDIT","Deposit Amt.","DEPOSIT","Deposit","Deposit Amount\r(INR )","Amount",
              "Credit (Rs.)","Withdrawal Amt. Deposit Amt.","Deposit Amount\r(INR )","Credit(Rs)","Withdrawals Deposits",
               "Cr Amount","Withdrawal (Dr)/","DEPOSITS","WITHDRAWALS"]

    debit_list = ["Withdrawal Amt.","Withdrawal","Withdrawal","DEBIT","Withdrawals","Debit","Withdrawal (Dr)"
              ,"Withdrawal Amt. Deposit Amt.","Withdrawal (Dr)/","Withdrawal Amount\r(INR )","Debit (Rs.)","Debit(Rs)",
             "WITHDRAWALS","Withdrawal INR","Withdrawal Amt","Amount","Withdrawal Amount","Withdrawals Deposits","WithDrawal",
             "Dr Amount"]


    balance_list = ["Balance","Closing Balance","BALANCE","Running Balance","BALANCE","Balance (INR )","Amount",
                "Running","Balance(Rs)","Total Amount\rDr/Cr"]

    test_data=df_list[0]
    col_len=test_data.shape[1]
    tab_cols=test_data.columns
    table_columns=[]
    row_index=[]
    for elem in range(len(tab_cols)):
        if tab_cols[elem] in col_list:
            col_name=tab_cols[elem]
            table_columns.append(col_name)
        else:
            table_columns.append("Unknown_column")
    uc_count=op.countOf(table_columns, "Unknown_column")
    if uc_count>=3 or len(table_columns)<=3:
        for row_ind in range(col_len-1):
            test_list=list(test_data[tab_cols[row_ind]])
            for i in range(len(col_list)):
                col_el=col_list[i]
                if col_el in test_list:
                    row_inde=test_list.index(col_el)
                    row_index.append(row_inde)
        if len(row_index)==0:
            if len(df_list)<= 4:
                lst_no=0
            else:
                lst_no=4
            data1=df_list[1]
            data2=df_list[2]
            data3=df_list[lst_no]
            data1_columns=[]
            data2_columns=[]
            data3_columns=[]
            page_data1=data1.values.tolist()
            page_data2=data2.values.tolist()
            page_data3=data3.values.tolist()
            data1_cols=data1.columns
            data2_cols=data2.columns
            data3_cols=data3.columns
            for elem in range(len(data1_cols)):
                if data1_cols[elem] in col_list:
                    col_name=data1_cols[elem]
                    data1_columns.append(col_name)
                else:
                    data1_columns.append("Unknown_column")
            for elem in range(len(data2_cols)):
                if data2_cols[elem] in col_list:
                    col_name=data2_cols[elem]
                    data2_columns.append(col_name)
                else:
                    data1_columns.append("Unknown_column")
            for elem in range(len(data3_cols)):
                if data3_cols[elem] in col_list:
                    col_name=data3_cols[elem]
                    data3_columns.append(col_name)
                else:
                    data3_columns.append("Unknown_column")            
            
            data1_count=op.countOf(data1_columns, "Unknown_column")
            data2_count=op.countOf(data2_columns, "Unknown_column")
            data3_count=op.countOf(data3_columns, "Unknown_column")
            data_uc_count=[data1_count,data2_count,data3_count]
            min_uc_index = data_uc_count.index(min(data_uc_count))
            dict_cols={0:data1_columns,1:data2_columns,2:data3_columns}
            dict_data={0:data1,1:data2,2:data3}
            data_tab_cols=dict_cols[min_uc_index]
            data_first=dict_data[min_uc_index]
            pdf_data=[]
            page_data0=data_first.values.tolist()
            pdf_data=pdf_data + page_data0
            pdf_data=pdf_data + page_data1
            pdf_data=pdf_data + page_data2
            pdf_data=pdf_data + page_data3
            
            for ls in range(len(df_list)):
                page_data=df[ls].values.tolist()
                pdf_data=pdf_data+page_data
            data1_pdf=pd.DataFrame(pdf_data)
            repete=data1_pdf.shape[1]-len(data_tab_cols)
            
            for add in range(repete):
                data_tab_cols.append('column_added')
            pdf_data=pd.DataFrame(pdf_data,columns= data_tab_cols)
            data_pdf=pdf_data.replace(np.nan,'')
            com_table=data_pdf
            com_table1=data_pdf
        
        elif min(row_index)>=2:
            test_data1=test_data.values.tolist()
            row_value=min(row_index)
            data1_col_list=test_data1[row_value]
            data2_col_list=test_data1[row_value+1]
            data_col_list=data1_col_list + data2_col_list
            columns_list=[]
            row_columns=[]
            
            for elem in range(len(data_col_list)):
                txt=data_col_list[elem]
                txt=str(txt)
                list_txt =list(txt.split())
                columns_list=columns_list+list_txt
            for elem in range(len(columns_list)):
                if columns_list[elem] in col_list:
                    col_name=columns_list[elem]
                    row_columns.append(col_name)
            data1=df_list[1]
            data1=data1.values.tolist()
            #data1=pd.DataFrame(data1,columns=row_columns)
            for lst_len in range(len(df_list)):
                page_data=df_list[lst_len]
                page_data=page_data.values.tolist()
                data1=data1+page_data
            pdf_data1=pd.DataFrame(data1)    
            repete=pdf_data1.shape[1]-len(row_columns)
            for add in range(repete):
                row_columns.append('column_added')
            pdf_data=pd.DataFrame(data1,columns=row_columns)
            pdf_data=pdf_data.replace(np.nan,'')
            com_table=pdf_data
            com_table1=pdf_data
        else:
            num_row=0
            pdf_data=[]
            pdf_data.append(list(df[num_row]))
            pdf_columns=list(df[num_row])
            for ls in range(len(df_list)-num_row):
                page_data=df[ls+num_row].values.tolist()
                pdf_data=pdf_data+page_data
            data_pdf=pd.DataFrame(pdf_data)
            data_pdf=data_pdf.replace(np.nan,'')
            repete=data_pdf.shape[1]-len(pdf_columns)
            for add in range(repete):
                pdf_columns.append('columns')
        
            data_pdf=data_pdf.rename(columns=data_pdf.iloc[0]).drop(data_pdf.index[0]) 
            data_pdf1=data_pdf.rename(columns=data_pdf.iloc[0]).drop(data_pdf.index[0])
            com_table=data_pdf
            com_table1=data_pdf1    
    else:
        num_row=0
        pdf_data=[]
        pdf_data.append(list(df[num_row]))
        pdf_columns=list(df[num_row])
        for ls in range(len(df_list)-num_row):
            page_data=df[ls+num_row].values.tolist()
            pdf_data=pdf_data+page_data
        data_pdf=pd.DataFrame(pdf_data)
        data_pdf=data_pdf.replace(np.nan,'')
        repete=data_pdf.shape[1]-len(pdf_columns)
        for add in range(repete):
            pdf_columns.append('columns')
        
        data_pdf=data_pdf.rename(columns=data_pdf.iloc[0]).drop(data_pdf.index[0]) 
        data_pdf1=data_pdf.rename(columns=data_pdf.iloc[0]).drop(data_pdf.index[0])
        com_table=data_pdf
        com_table1=data_pdf1
    cols = list(com_table.columns)
    cols1 = list(com_table1.columns)
    #cols2 = list(com_table2.columns)
    for i in range(len(cols)):
        if cols[i] in date_list:
            date=cols[i]
            date_ind=i
    for j in range(len(cols1)):
        if cols1[j] in date_list:
            date=cols1[j]
            date_ind=j
    for k in range(len(cols)):
        if cols[k] in narration_list:
            narration=cols[k]
            nar_ind=k
    for l in range(len(cols1)):
        if cols1[l] in narration_list:
            narration=cols1[l]
            nar_ind=l
    for m in range(len(cols)):
        if cols[m] in credit_list:
            credit=cols[m]
            credit_ind=m 
    for n in range(len(cols1)):
        if cols1[n] in credit_list:
            credit=cols1[n]
            credit_ind=n 
    for dbt in range(len(cols)):
        if cols[dbt] in debit_list:
            debit=cols[dbt]
            debit_ind=dbt
    for dbt1 in range(len(cols1)):
        if cols1[dbt1] in debit_list:
            debit=cols1[dbt1]
            debit_ind=dbt1
    for blns in range(len(cols)):
        if cols[blns] in balance_list:
            balance=cols[blns]
            balance_ind=blns
    for blns1 in range(len(cols1)):
        if cols1[blns1] in balance_list:
            balance=cols1[blns1]
            balance_ind=blns1
    Transaction_date =list(com_table[cols[date_ind]])
    Narration = list(com_table[cols[nar_ind]])
    Deposits=list(com_table[cols[credit_ind]])
    Debit = list(com_table[cols[debit_ind]])
    Balance = list(com_table[cols[balance_ind]])
    data4=pd.DataFrame(Transaction_date,columns=["Transaction Date"])
    data5 = pd.DataFrame(Narration,columns=["Narration"])
    data6 = pd.DataFrame(Deposits,columns=["Credit"])
    data7 = pd.DataFrame(Debit,columns=["Debit"])
    data8 = pd.DataFrame(Balance, columns= ["Balance"])
    data=data4.join(data5)
    data=data.join(data6)
    data=data.join(data7)
    data =data.join(data8)
    data=data.replace(np.nan,'')
    axis_list=["axis-bank","Axis Bank  India","Axis Bank  India","AXIS (UTI) Bank","Axis Bank India","Axis Bank, India",
                   "Axis Ban","Axis Bank","Axis Bank Ltd","Axis Bank Ltd.","Axis Bank ","Axis","axis","AXIS"]

    if bank_name in axis_list:
        for ele in range(len(Narration)-1):
            if Transaction_date[ele] == '' and Balance [ele]== '':
                Narration[ele+1]=str(Narration[ele])+str(Narration[ele+1])
    else:
        for ele in range(len(Narration)):
            if Transaction_date[ele] == '':
                Narration[ele-1]=str(Narration[ele-1])+str(Narration[ele])
    
    Transaction_date=pd.DataFrame(Transaction_date,columns=["Transaction Date"])
    Narration= pd.DataFrame(Narration,columns=["Narration"])
    Deposits = pd.DataFrame(Deposits,columns=["Credit"])
    Debit = pd.DataFrame(Debit,columns=["Debit"])
    Balance = pd.DataFrame(Balance,columns=["Balance"])
    data=Transaction_date.join(Narration)
    data=data.join(Deposits)
    data=data.join(Debit)
    data=data.join(Balance)
    #data=data.replace('',np.nan)
    #data=data.dropna()
    txn_date = list(data["Transaction Date"])
    cr_list=list(data["Credit"])
    dr_list=list(data["Debit"])
    bls_list=list(data["Balance"])
    row_index=[]
    for row_num in range(len(data["Narration"])):
        if txn_date[row_num]== '':
            a=row_num
            row_index.append(a)
        elif cr_list[row_num]== '' and dr_list[row_num]== '' and bls_list=='' :
            b=row_num
            row_index.append(b)
    unique_row_index = []
    for x in range(len(row_index)):
        if row_index[x] not in unique_row_index:
            row_ind=row_index[x]
            unique_row_index.append(row_ind)
    data=data.drop(unique_row_index,axis=0)
    salary1 = data[data["Narration"].str.contains("SALARY")]
    salary2 = data[data["Narration"].str.contains("Salary")]
    sala_cr= data[data["Narration"].str.contains("CREDIT")]
    salary3 = data[data["Narration"].str.contains("salary")]
    sal_ac = data[data["Narration"].str.contains("SAL")]
    sal_fl = data[data["Narration"].str.contains("Sal")]
    #sal_al = data[data["Narration"].str.contains("sal")]
    NEFT = data[data["Narration"].str.contains("NEFT")]
    IMPS = data[data["Narration"].str.contains("IMPS")]
    sal=sal_ac.append(sal_fl)
    #sal = sal.append(sal_al)
    salary=salary1.append(salary2)
    salary=salary.append(salary3)
    salary=salary.append(sal)
    salary=salary.drop_duplicates(subset="Narration")
    #dataframe.drop_duplicates(subset, keep, inplace, ignore_index)
    UPI = data[data["Narration"].str.contains("UPI")]
    NACH = data[data["Narration"].str.contains("NACH")]
    ACH = data[data["Narration"].str.contains("ACH")]
    NACH=NACH.append(ACH)
    
    ecs=["ECSRTN","ECSRTNCHGS","NACH_AD,RTN_CHRG","ACH DEBIT RETURN CHARGES","EMI RTN CHARGES","NACH RTN CHG","Chrg:Ecs Return",
    "Chrg:Ecs Mandate","ECS DR RTN","NACH RETURN CHARGES","ECS Return","Bounce Charges","ACH RTN","Debit Return Charges","NACH Return",
    "RTN Charges","ECS/ACH RETURN","ACH D","ACH RETURN","ACH DEBIT RETURN"]
    
    fantasy_gaming=["Rummy","rummy","Junglee","junglee","Mpl","mpl","Dream11","dream11","Adda52","adda52","Ace2three","ace2three",
                   "Poker","poker","Rummy Circle","Pokerbaazi","pokerbaazi","Ace2Three","My11Circle"]
    
    ecs_rtn = data[data["Narration"].str.contains("ECSRTN")]
    ecs_col=list(ecs_rtn.columns)
    ecs_rtn_data=ecs_rtn.values.tolist()
    for es in range(len(ecs)):
        ecs_name=ecs[es]
        ecs1 = data[data["Narration"].str.contains(ecs_name)]
        ecs1_data = ecs1.values.tolist()
        ecs_list =ecs_rtn_data + ecs1_data
    ecs_tab=pd.DataFrame(ecs_list,columns=ecs_col)
    gaming = data[data["Narration"].str.contains("ummy")]
    gm_col=list(gaming.columns)
    gm_rtn_data=gaming.values.tolist()
    for es in range(len(fantasy_gaming)):
        gm_name=fantasy_gaming[es]
        gm1 = data[data["Narration"].str.contains(gm_name)]
        gm1_data = gm1.values.tolist()
        gm_list =gm_rtn_data + gm1_data
    gm_tab=pd.DataFrame(gm_list,columns=gm_col)    
    data_frame=data.to_json()
    bankData = data.T
    #print(bankData)
    data_json = bankData.to_json()
    upi_json=UPI.T.to_json()
    #print(data_json)
    #print(upi_json)
    return data_json

#bank_name = "icici_bank"
#file_name= 'C:/Users/VSK/Desktop/Bank_Statement/Bank statement/APP1672081012392347.pdf'
#bank_stament_read(file_name,bank_name)        

from flask import Flask, jsonify, request #import objects from the Flask model
import json
app = Flask(__name__) #define app using Flask    

@app.route('/bankstatement', methods=['POST'])
def bankStatement():
    bs = { "file_name": request.json['file_name'], "bank_name":request.json['bank_name']}
    bank = bank_stament_read(bs["file_name"],bs["bank_name"]) 
    return (bank)

if __name__ == '__main__':
	app.run(debug=True, port=8080) #run app on port 8080 in debug mode
