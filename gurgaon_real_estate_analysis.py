import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('../data/data of gurugram real Estate.csv')

print(df.head())
print(df.info())


# Data Cleaning

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

print(df.columns.tolist())

# Remove duplicates
df = df.drop_duplicates()


# Numerical Columns Cleaning

df['price'] = df['price'].astype(str).str.replace(',', '').astype(float)

df['area'] = df['area'].astype(str).str.replace(',', '').astype(int)

df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int)


# Categorical Columns Cleaning

df['status'] = df['status'].str.strip().str.lower().astype(object)

df['rera_approval'] = (
    df['rera_approval']
    .str.strip()
    .str.lower()
    .map({
        'approved by rera': True,
        'not approved by rera': False
    })
)

df['flat_type'] = df['flat_type'].str.strip().str.lower().astype(object)

df['property_type'] = df['property_type'].str.strip().astype(object)

df['locality'] = df['locality'].str.strip().astype(object)

df['builder_name'] = df['builder_name'].str.strip().astype(object)

df['society'] = df['society'].str.strip().astype(object)

df['company_name'] = df['company_name'].str.strip().astype(object)


# Remove duplicates after cleaning
df = df.drop_duplicates()


# Final Output

#print(df)
#print(df.info())

# Question 1: Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat in the dataset is a {costliest_flat['property_type']} located in {costliest_flat['locality']} with a price of {costliest_flat['price']/10000000}crores. It has an area of {costliest_flat['area']} sqft and a rate per sqft of {costliest_flat['rate_per_sqft']}. The builder is {costliest_flat['builder_name']} and it is {'RERA approved' if costliest_flat['rera_approval'] else 'not RERA approved'}.")

# Question 2: Which locality has the highest average price?
locality_avg_price = df.groupby('locality')['price'].mean().idxmax()
print(f"Locality with the highest average price: {locality_avg_price}")

# Question 3: Which locality has the highest rate per square foot?
locality_avg_rate = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"Locality with the highest rate per square foot: {locality_avg_rate}")

# Question 4: Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more than under-construction properties.")
else:
    print("Under-construction properties cost more than ready-to-move properties.")

# Question 5: Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
if rera_approved_avg_price > not_rera_approved_avg_price:
    print("RERA-approved properties command a price premium.")
else:
    print("RERA-approved properties do not command a price premium.")

# Question 6: How does area (sqft) impact property price?
area_price_correlation = df['area'].corr(df['price'])
print(f"Correlation between area and price: {area_price_correlation}")

# Question 7: Which BHK configuration is the most expensive on average?
bhk_avg_price = df.groupby('bhk_count')['price'].mean().idxmax()
print(f"BHK configuration with the highest average price: {bhk_avg_price}")

# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
property_type_avg_price = df.groupby('property_type')['price'].mean().idxmax()
print(f"Property type with the highest average price: {property_type_avg_price}")

# Question 9: Do certain builders or companies consistently price higher?
builder_avg_price = df.groupby('builder_name')['price'].mean().idxmax()
company_avg_price = df.groupby('company_name')['price'].mean().idxmax()
print(f"Builder with the highest average price: {builder_avg_price}")
print(f"Company with the highest average price: {company_avg_price}")

# Question 10: Are larger homes always more expensive per square foot?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.savefig('../visualizations/area_vs_rate_per_sqft.png', dpi=150, bbox_inches='tight')
plt.show()
