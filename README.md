# Heritage Housing Price Prediction

![Am I Responsive Image](static/images/amiresponsivePP5.PNG)

Welcome to the **Heritage Housing Price Prediction** project! This tool is designed to support **local councils, planners, and conservation teams** in evaluating and forecasting the market value of **heritage-listed properties**, with a focus on fairness, transparency, and data-driven decision making.

### Project Highlights

- **Predictive Model**: Accurately forecasts sale prices for both standard and heritage homes, including a test set of inherited properties.
- **Interactive Visualizations**: Explore relationships between structural and historical property features and sale prices.
- **User-Centric Dashboard**: Built using Streamlit for clear, actionable insights and real-time property valuation predictions.

## Dataset Content

### Source

The datasets used in this project were provided as part of the Code Institute's Predictive Analytics module. They consist of real-world housing records and client-specific inherited properties.

### Licensing

All datasets are shared under open licenses with no ethical or privacy concerns. The data is anonymized and suitable for academic and analytical purposes.

### Structure

The project includes the following key datasets:

- `house_prices_records.csv`  
  - **Size**: 1460 rows × 24 columns  
  - **Content**: Detailed historical housing records including structural features, quality ratings, and sale prices.  
  - **Purpose**: Used for training and evaluating machine learning models.

- `inherited_houses.csv`  
  - **Size**: 4 rows × 23 columns  
  - **Content**: Feature data for four heritage-listed houses inherited by the client.  
  - **Note**: Sale prices are excluded and will be predicted by the model.  
  - **Purpose**: Used for inference and testing of the final prediction pipeline.

### Detailed Feature Descriptions  

The datasets include attributes such as lot area, year built, overall quality, and living area size. Additional engineered features like **Age**, **LivingLotRatio**, and **FinishedBsmtRatio** were added during preprocessing to enhance model performance.

### Dataset Quality and Observations  

- The raw `house_prices_records.csv` contained missing values in fields like `LotFrontage`, `GarageYrBlt`, and `MasVnrArea`.
- The `inherited_houses.csv` was mostly clean and required only minimal processing.
- All datasets were thoroughly validated, cleaned, and stored in the `data/processed/` directory for traceability.

### Data Limitations

- Imputation may introduce slight biases due to missing data.
- The dataset is limited to a specific geographic context (e.g., Ames, Iowa), which may affect generalizability.
- Outliers were addressed but remain a consideration in model performance.

## Business Requirements

The client—representing a local planning authority—has inherited four **heritage-listed residential properties** and seeks support in evaluating their fair market value. Due to regulatory constraints and the unique nature of heritage properties, traditional valuation approaches may fall short. This project provides a **data-driven approach** to forecasting prices, identifying key value drivers, and ensuring consistent and transparent appraisals.

### Key Client Goals

- **Understand Attribute Correlations**  
  Identify which structural and historical features most strongly influence sale prices. This helps ensure heritage valuation is not skewed by subjective or outdated assumptions.

- **Predict Fair Market Prices**  
  Use a robust regression model to predict sale prices for the inherited properties and other heritage homes, aligned with market benchmarks.

- **Enable Strategic Planning**  
  Support data-backed planning, resource allocation, and potential redevelopment efforts by offering clear pricing insights.

### Context & Relevance

Heritage properties are unique due to architectural preservation, age, and location factors. This model addresses the valuation challenges by training on a comprehensive dataset, engineering features that reflect property age and use, and testing accuracy on held-out and inherited data.

### Deliverables

- **Correlational Insights**: Interactive visualizations of the most important features (e.g., `OverallQual`, `GrLivArea`, `GarageArea`) and their relationship with sale prices.
- **Predictive Model**: A trained machine learning model capable of predicting property values with high accuracy.
- **Dashboard Interface**: A Streamlit dashboard where users can:
  - Explore correlations,
  - Predict property prices in real time,
  - Review technical details of the modeling process.

## Hypotheses and Validation Plan

This project is grounded in data-driven hypotheses about what influences house prices, especially in the context of heritage properties. Each hypothesis has been validated through statistical analysis, visual inspection, and model performance evaluation.

### Hypotheses

#### Attribute Correlation

- Features such as **Overall Quality (OverallQual)**, **Above Ground Living Area (GrLivArea)**, and **Garage Area (GarageArea)** are expected to show **strong positive correlations** with sale prices.
- Attributes like **Year Built**, **Basement Finish Type**, and **Lot Area** are hypothesized to show **moderate influence** on sale prices.
- New engineered features like **Age**, **LivingLotRatio**, and **FinishedBsmtRatio** may add significant predictive power.

#### Predictive Model

- A regression model trained on the cleaned dataset will achieve an **R² score ≥ 0.75**, demonstrating strong generalization on unseen test data.
- The model should produce **realistic predictions** for the 4 inherited heritage properties, aligning with similar homes in the dataset.

### Validation Plan

#### Attribute Correlation Validation

- **Statistical Analysis**:  
  - Compute Pearson and Spearman correlation coefficients to quantify relationships.
- **Visualizations**:  
  - Create heatmaps, scatter plots, and bar charts for numeric and categorical variables.
- **Feature Ranking**:  
  - Rank features by correlation strength and SHAP importance.

#### Predictive Model Validation

- **Model Training**:  
  - Train multiple regressors (Linear Regression, Random Forest, XGBoost).
- **Evaluation Metrics**:  
  - Use R², MAE, and RMSE to assess predictive accuracy.
- **Cross-Validation**:  
  - Apply k-fold validation to assess model stability and prevent overfitting.

#### Inherited Properties Prediction

- **Input Features**:  
  - Use top-ranked features to predict sale prices for the 4 inherited houses.
- **Comparison**:  
  - Cross-check predictions against the broader Ames market trend distribution.
- **Deliverable**:  
  - Provide individual predictions and an aggregated total value for the 4 properties.

## Mapping Business Requirements to ML Tasks

Each business requirement has been directly translated into specific data visualizations, machine learning tasks, and dashboard functionalities. This ensures that all stakeholder goals are addressed in a measurable, transparent, and interactive manner.

### Business Requirement: Understanding Attribute Correlations

**Goal**: Identify key features driving the price of heritage-listed properties.

**Approach**:

- **Data Visualizations**
  - Heatmaps to show Pearson/Spearman correlations.
  - Scatter plots for features like `GrLivArea`, `OverallQual`, `GarageArea` vs `SalePrice`.
  - Bar charts to assess categorical features (e.g., `KitchenQual`, `BsmtFinType1`) and sale price.

- **ML Tasks**:  
  - Correlation analysis using both statistical and visual tools.
  - Feature importance extraction from Random Forest and XGBoost models.

- **Dashboard Integration**:  
  - Interactive heatmaps and scatter plots.
  - Dropdowns and filters for user-driven exploration of correlations.

### Business Requirement: Predicting Sale Prices

**Goal**: Estimate the market value of inherited heritage homes and other properties.

**Approach**:

- **ML Tasks**:  
  - Train regression models (Linear, Random Forest, XGBoost) on engineered and cleaned features.
  - Use evaluation metrics (R², MAE, RMSE) to compare performance.
  - Perform hyperparameter tuning using GridSearchCV or RandomizedSearchCV.

- **Dashboard Integration**:  
  - Interactive input form for users to enter property attributes.
  - Real-time price prediction output.
  - Display model accuracy and key metrics for transparency.

### Business Requirement: Unified Interface for Insights and Prediction

**Goal**: Deliver a centralized, user-friendly tool to both explore data and make predictions.

**Approach**:

- **Dashboard Features**:  
  - Navigation to explore:
    - Attribute correlations
    - Hypothesis validation
    - Price predictions
    - Technical summary

  - Outputs presented via:
    - Charts
    - Tables
    - Downloadable prediction results

## ML Business Case

Machine learning plays a central role in this project by enabling accurate, automated, and scalable valuation of heritage properties. By capturing non-linear interactions between features and prices, ML models provide insights that go beyond traditional appraisal methods.

### Objectives of Machine Learning

- **Accurate Price Forecasting**:  
  Train a regression model capable of predicting fair market prices for both standard and heritage properties, using historical sale data and engineered features.

- **Feature Impact Analysis**:  
  Identify which property characteristics (e.g., `OverallQual`, `Age`, `GarageArea`) have the strongest influence on sale prices.

- **Real-Time Usability**:  
  Integrate ML predictions into a dashboard interface where users can enter property details and receive instant valuation output.

### Why Machine Learning?

- **Data-Driven Decision Making**:  
  Removes subjectivity in heritage valuations and ensures consistency.

- **Complex Relationship Handling**:  
  Models like Random Forest and XGBoost capture intricate, non-linear patterns that traditional valuation methods often miss.

- **Scalability**:  
  Once trained, the model can handle new property inputs and scale across additional use cases without rework.

- **Evaluation Metrics for Confidence**:  
  Metrics like R², MAE, and RMSE are used to validate performance, making results explainable and trustworthy.

## User Stories

User stories were created to define functional requirements and ensure the project stays aligned with the client’s real-world needs. These stories guided the design of the dashboard, the machine learning pipeline, and the visual outputs.

The full list of user stories for this project can be found [here](https://github.com/users/EktaMehra/projects/5/views/1).

## Dashboard Design

The dashboard serves as the user-facing interface of the Heritage Housing project. Built with **Streamlit**, it presents predictions and insights in a clear, interactive, and accessible format—suitable for both technical and non-technical users.

### Design Philosophy

- **Simplicity**: Focused on intuitive layouts with minimal clutter.
- **Usability**: Easy navigation across pages for correlational insights, hypothesis validation, predictions, and technical transparency.
- **Responsiveness**: Designed to be compatible with desktop and tablet environments.

### Dashboard Structure (Add All the images)

The application is divided into the following pages:

1. **Main Page**  
   - Instructs users to use the sidebar to navigate to all app features.

2. **Home**  
   - Overview of the project and its goals.  
   - Brief context on the client’s challenge and use case.

3. **Feature Correlation**  
   - Interactive heatmaps and scatter plots to explore attribute relationships.  
   - Dropdown selectors for numeric and categorical feature comparison.

4. **Hypothesis Validation**  
   - Visual evidence to support or refute project hypotheses.  
   - Commentary on findings from correlation and modeling.

5. **Price Prediction**  
   - Input form for custom property details.  
   - Real-time sale price prediction output and table of inputs.  
   - Display of inherited property predictions and total valuation.

6. **Technical Summary**  
   - Overview of the data pipeline, model evaluation, and performance metrics.  
   - Downloadable charts and summaries for transparency.

7. **User Guide**  
   - Step-by-step instructions on how to use the app.  
   - Descriptions of each page and expected user inputs/outputs.

### Future Enhancements

- Add user feedback collection mechanism.
- Include localised property benchmarks for cross-region comparison.
- Incorporate feature importance visualisations per prediction.

## Methodology

This project follows the **CRISP-DM** (Cross-Industry Standard Process for Data Mining) framework, ensuring a structured and repeatable approach to data science. It also incorporates Agile-inspired iteration and validation throughout the project lifecycle.

### Business Understanding

**Goal**:  
Help local authorities and property owners estimate fair market prices for heritage-listed homes using a data-driven model.

**Client Objectives**:

- Understand which property attributes influence value.
- Predict sale prices for 4 inherited properties.
- Support transparent, consistent property valuations.

### Data Understanding

**Activities**:

- Reviewed raw datasets (`house_prices_records.csv` and `inherited_houses.csv`).
- Identified missing values, outliers, and data types.
- Explored distributions and key summary statistics.

**Observations**:

- `house_prices_records.csv` had missing values in key columns (`LotFrontage`, `GarageYrBlt`).
- `inherited_houses.csv` was cleaner but excluded `SalePrice`.

### Data Preparation

**Steps Taken**:

- Imputed missing values using domain-informed techniques.
- Dropped low-importance or high-null columns.
- Removed duplicates and standardized data types.
- Created new features: `Age`, `LivingLotRatio`, `FinishedBsmtRatio`.

**Output**:

- Cleaned datasets saved to `data/processed/`
- Train-test split completed and versioned.

### Modeling

**Approach**:

- Tested multiple regression algorithms: Linear Regression, Random Forest, XGBoost.
- Performed hyperparameter tuning using `GridSearchCV`.
- Evaluated models on a hold-out test set using:
  - **R² Score**
  - **MAE (Mean Absolute Error)**
  - **RMSE (Root Mean Squared Error)**

**Selected Model**:

- Random Forest Regressor based on best validation performance.

### Evaluation

**Test Dataset**:

- R² Score > 0.75 achieved.
- Residuals and prediction plots analyzed for consistency.

**Inherited Properties**:

- Predictions generated for the 4 client properties.
- Results compared against Ames market benchmarks to ensure realism.

### Deployment

**Implementation**:

- Final pipeline serialized and saved.
- Dashboard developed in **Streamlit**, integrated with trained model and visual outputs.

**Interface**:

- Users can explore data relationships, validate hypotheses, and generate real-time predictions via sidebar navigation.

## Project Features & Outcomes

This section summarizes the key deliverables of the Heritage Housing project and how they directly address the business requirements and client goals.

---

### Project Features

- **Data Cleaning and Preparation**  
  - Cleaned and standardized housing datasets.
  - Imputed missing values, removed irrelevant columns, and ensured data integrity.
  - Engineered new features (`Age`, `LivingLotRatio`, `FinishedBsmtRatio`) to boost model insight.

- **Exploratory Data Analysis (EDA)**  
  - Statistical and visual analysis of all numeric and categorical features.
  - Correlation matrix and scatter plots to identify high-impact features.

- **Feature Selection & Modeling**  
  - Correlation- and SHAP-based feature ranking.
  - Trained and optimized multiple regressors: Linear, Random Forest, and XGBoost.

- **Prediction Interface**  
  - Real-time model deployed via Streamlit for sale price predictions.
  - Inherited property valuation with summary output.

- **Interactive Dashboard**  
  - Feature correlation exploration
  - Hypothesis validation charts
  - Live prediction form and results
  - Technical summary of model performance

---

### Project Outcomes

#### Business Requirement 1: Attribute Correlation  

- Delivered heatmaps, scatter plots, and ranked feature lists.  
- Highlighted `OverallQual`, `GrLivArea`, `GarageArea`, and `Age` as key drivers.

#### Business Requirement 2: Sale Price Prediction  

- Final Random Forest model achieved **R² > 0.75** on test data.  
- Successfully predicted market-aligned prices for all 4 inherited properties.

#### Dashboard  

- Fully functional, responsive interface with intuitive navigation.  
- Enables non-technical users to gain insights and generate predictions.

## Testing

Thorough testing was conducted to ensure the accuracy, reliability, and usability of both the machine learning model and the dashboard interface. Testing spanned data preprocessing, model performance, and front-end interactions.

### Unit Testing

**Purpose**: Ensure correctness of individual preprocessing steps and feature engineering functions.

**Key Areas Tested**:

- **Missing Value Imputation**: Verified replacements were applied correctly.
- **Feature Creation**: Checked that `Age`, `LivingLotRatio`, and `FinishedBsmtRatio` were computed and added accurately.
- **Data Splits**: Confirmed reproducibility of train/test splits and absence of leakage.

### Model Evaluation

**Purpose**: Validate the predictive performance of the trained models.

**Metrics Used**:

- **R² Score**: Assesses model fit.
- **MAE**: Evaluates average prediction error.
- **RMSE**: Highlights magnitude of larger errors.

**Process**:

- Final model (Random Forest) achieved **R² > 0.75** on test data.
- Inherited property predictions aligned with local market expectations.
- Residual plots reviewed to confirm no major bias or variance issues.

### Dashboard Testing

**Purpose**: Ensure functional stability and user interaction integrity.

**Testing Areas**:

- **Navigation**: Verified smooth switching between pages via sidebar.
- **Widgets**: Confirmed correct operation of dropdowns, sliders, number inputs, and prediction buttons.
- **Visualizations**: All plots rendered correctly and updated dynamically.
- **Prediction Logic**: Validated that model outputs updated in real time based on inputs.
- **Output Format**: Checked for clear, readable presentation of results and prediction summaries.

---

### Compatibility & Manual Checks

- Tested across browsers (Chrome, Edge, Firefox).
- Simulated various input edge cases to ensure robustness and error handling.

> No known bugs or broken features were observed at the time of submission.

## Deployment

The Heritage Housing dashboard was deployed using **Streamlit**, making the tool publicly accessible for stakeholders and users to interact with the model and visualizations in real time.

### Deployment Steps

1. **Prepare Final Pipeline**  
   - Serialized the trained Random Forest model, fitted scaler, and feature pipeline using `joblib`.
   - Saved necessary outputs (e.g., prediction-ready dataset, evaluation metrics) to `/outputs/`.

2. **Streamlit App Structure**  
   - Created modular Python scripts for each dashboard page (Home, Prediction, Feature Correlation, etc.).
   - Integrated all backend logic and visuals within a clean sidebar navigation UI.

3. **Set up Hosting Environment**  
   - Used **Streamlit Community Cloud** for hosting the app.
   - Defined `requirements.txt` to specify necessary libraries.
   - Set a lightweight `.slugignore` to exclude large files (e.g., raw CSVs and intermediate figures) not needed at runtime.

4. **Connect to GitHub**  
   - Linked the GitHub repo to Streamlit Cloud for continuous deployment.
   - Updates pushed to main are automatically reflected in the live app.

### Deployment Considerations

- **Slug Size**:  
  `.slugignore` was configured to avoid unnecessary files and keep the app within platform limits.
  
- **Reproducibility**:  
  All model artefacts are versioned in the `/outputs/models/` and `/outputs/pipelines/` directories.

- **Performance**:  
  Dashboard optimized for responsiveness; pre-computed artefacts are loaded rather than recalculated on each session.

---

## Technologies Used

A variety of tools and libraries were used to support data cleaning, exploratory analysis, model development, and dashboard deployment. The stack ensures robustness, interactivity, and maintainability.

### Programming Language

- **Python**: Primary language used for data processing, modeling, and dashboard development.

### Key Libraries and Frameworks

#### Data Handling

- **pandas**: Data manipulation and wrangling.
- **numpy**: Numerical operations and matrix handling.

#### Data Visualization

- **matplotlib**: Core plotting library.
- **seaborn**: Statistical graphics for heatmaps, bar plots, and KDE plots.
- **plotly**: Interactive visualizations in the Streamlit app.

#### Feature Engineering and Preprocessing

- **scikit-learn**: Preprocessing, model selection, evaluation metrics.
- **Feature-engine**: Advanced feature transformation and selection.
- **joblib**: Model serialization and pipeline saving.

#### Machine Learning

- **scikit-learn**: Regression models and evaluation.
- **xgboost**: Gradient boosting model for performance benchmarking.

#### Model Interpretation

- **SHAP**: Feature importance and interpretability (used in development but not directly in the dashboard).

### Dashboard and Deployment

- **Streamlit**: Framework for building the interactive web app.
- **Streamlit Community Cloud**: Hosting environment for public app deployment.
- **Git/GitHub**: Version control and continuous deployment pipeline.

---

## Credits

### Data Sources

- **Kaggle - Ames Housing Dataset**: Provided by Code Institute as the core dataset for training and evaluation.
- **Inherited Houses Dataset**: A client-specific dataset containing 4 heritage properties without sale prices.

### Educational Resources

- **Code Institute**: Predictive Analytics course materials, mentor support, and assessment guidelines.
- **Churnometer Walkthrough Project**: Used as a structural and methodological reference.

### Tools and Packages

- **Streamlit Documentation**: Referenced for dashboard configuration and component integration.
- **scikit-learn, seaborn, pandas**: Official documentation consulted throughout development.

---

## Acknowledgements

- **Code Institute**: For providing project templates, walkthroughs, and the assessment framework.
- **My Mentor- Moritz**: For timely guidance during my entire journey of learning how to code.
- **Slack Community**: For peer discussions and troubleshooting ideas.
- **Tonicha B’s Property Value Analytics Project**: Referenced for structural inspiration, page layout design, and presentation approach.
- **ChatGPT**: Used for technical explanations and debugging during the project.

> Thank you to everyone who contributed directly or indirectly to the successful completion of this project.
