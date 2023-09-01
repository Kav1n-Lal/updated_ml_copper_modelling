# updated_ml_copper_modelling
- ## Problem_statement_link
-  [https://docs.google.com/document/d/1nWKUnD6F76F1AtGFEjyfIVH9oxcBUU1N/edit]
- ## Introduction video
- [https://drive.google.com/file/d/1ZpcgdM-G1-zPdOOEad6GxgShMGkZUyHs/view?usp=sharing]
- ## Regression task explanation video
- [https://drive.google.com/file/d/1w9JQxr-Z_NstZJgLUXkKEFEz4RhO2rtr/view?usp=sharing]
- ## Classification task explanation video
- [https://drive.google.com/file/d/1QqQbKq40MBsv_PavCmUpP5w-fWYn6jbh/view?usp=sharing]
- ## Streamlit app demonstration video
- [https://drive.google.com/file/d/1cSlWyN8VVc5VIJ3THMbCgyxtShBEPU-z/view?usp=sharing] 

## Other
- Download all the files in this repository
- The aim of this project is to predict copper selling price(regression) and copper status(classification) and create a user interactable app using streamlit to predict copper selling price and status.
- Create a new environment called 'ml_coppermodelling' using conda prompt.Ref link [https://www.youtube.com/watch?v=xl0N7tHiwlw&t=1806s]
- Run **revised_regressor_final.ipynb** file,you will get **rev_saved_steps_regressor.pkl** file.(TO PREDICT COPPER SELLING PRICE)
- Similarly run **revised_classifier_final.ipynb** file,you will get **rev_saved_steps_classifier.pkl** file.(TO PREDICT COPPER STATUS)
- The other .ipynb files(*CopperModelling_1,CopperModelling_2,copper_modelling_classifier*) contains Data preprocessing,various model training and evaluation,feature selections I did before finding out the best model.
- - ## Regression R2 score Table
|    Model             |  Train(R2-score)   |  Test(R2-score)   |
| :------------------- | -----------------  |-----------------: |
| Linear Regression    |      0.727         |0.707              |
| (Lin-reg,Yeo-Johnson)|      0.731         |0.710              |
| LassoCV              |      0.731         |0.710              |
| RidgeCV              |      0.731         |0.710              |
| ElasticNetCV         |      0.731         |0.710              |
| Polynomial Reg(deg-2)|      0.833         |0.820              |
| Polynomial Reg(deg-3)|      0.898         |0.888              |
| Polynomial Reg(deg-4)|      0.908         |0.893              |
| DecisionTree         |      0.959         |0.933              |
| RandomForest         |      0.958         |0.940              |
|ExtraTreesRegressor|1.00        |0.931  
|HistGradientBoostingRegressor|0.989        |0.969              |
- ## Classification ROCAUC score and Accuracy Table
|    Model             |  Train(ROC-AUC)   |  Test(ROC-AUC)   |Accuracy
| :------------------- | -----------------  |-----------------|-----------------: 
| RandomForestClassifier    |      0.972         |0.951             |0.871
| ExtraTreesClassifier|      0.983         |0.961              |0.895
| XGBClassifier             |      0.974         |0.938              |0.871
| HistGradientClassifier            |      0.984         |0.951              |0.899
# HistGradientBoostingRegressor and  HistGradientBoostingClassifier models performance is good
- Now launch vscode using the 'ml_coppermodelling' environment.
- On the VScode terminal,type 'streamlit run rev_prediction_app.py'
- The app is now deployed
- ## Screenshots from the app
![Screenshot (252)](https://github.com/Kav1n-Lal/updated_ml_copper_modelling/assets/116146011/7cb58c8d-3aa4-4539-8fc1-b6211a7810ea)
![Screenshot (253)](https://github.com/Kav1n-Lal/updated_ml_copper_modelling/assets/116146011/d5e6c91f-2e1b-4439-9dbd-c1b5ed83a988)
![Screenshot (254)](https://github.com/Kav1n-Lal/updated_ml_copper_modelling/assets/116146011/dda9aaff-1d93-4493-9826-5169cb476bdb)
![Screenshot (255)](https://github.com/Kav1n-Lal/updated_ml_copper_modelling/assets/116146011/00845b13-87ce-4ed4-b284-e9f9a1f03cdb)
![Screenshot (256)](https://github.com/Kav1n-Lal/updated_ml_copper_modelling/assets/116146011/206f9df5-2230-416d-ac99-739abf790507)

