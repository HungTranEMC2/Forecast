import mysql.connector
import pandas as pd

def load_apps_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS APPS (
            id VARCHAR(255) PRIMARY KEY,
            url VARCHAR(255),
            title VARCHAR(255),
            developer VARCHAR(255),
            developer_link VARCHAR(255),
            icon VARCHAR(255),
            rating FLOAT ,
            reviews_count INT,
            pricing_hint VARCHAR(255),
            lastmod timestamp
        )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (id, url, title, developer, developer_link, icon, rating, reviews_count,pricing_hint,lastmod)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_query, (row['id'],row['url'],row['title'],row['developer'],row['developer_link'],row['icon'],row['rating'],row['reviews_count'],row['pricing_hint'],row['lastmod']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
def load_reviews_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS REVIEWS (
            app_id VARCHAR(255) PRIMARY KEY,
            author VARCHAR(255),
            rating VARCHAR(255),
            posted_at timestamp,
            body VARCHAR(255),
            developer_reply VARCHAR(255),
            developer_reply_posted_at timestamp,
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (app_id, author, rating, posted_at, body, developer_reply, developer_reply_posted_at)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(insert_query, (row['app_id'],row['author'],row['rating'],row['posted_at'],row['body'],row['developer_reply'],row['developer_reply_posted_at']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()    
    
def load_pricing_plans_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS PRICING_PLANS (
            id VARCHAR(255) PRIMARY KEY,
            app_id VARCHAR(255),
            title VARCHAR(255),
            price VARCHAR(255),
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (id, app_id, title, price)
        VALUES (%s,%s,%s,%s)
        """
        cursor.execute(insert_query, (row['id'],row['app_id'],row['title'],row['price']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()        
    
def load_key_benefits_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS KEY_BENEFITS (
            app_id VARCHAR(255) PRIMARY KEY,
            description VARCHAR(255),
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (app_id, description)
        VALUES (%s,%s)
        """
        cursor.execute(insert_query, (row['app_id'],row['description']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()            
    
def load_apps_categories_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS APPS_CATEGORIES (
            app_id VARCHAR(255) PRIMARY KEY,
            category_id VARCHAR(255),
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (app_id, category_id)
        VALUES (%s,%s)
        """
        cursor.execute(insert_query, (row['app_id'],row['category_id']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()                

def load_categories_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS CATEGORIES (
            id VARCHAR(255) PRIMARY KEY,
            title VARCHAR(255),
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (id, title)
        VALUES (%s,%s)
        """
        cursor.execute(insert_query, (row['id'],row['title']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()         
    
def load_pricing_plan_features_table(df, db_config):
    #Establish a database connection
    conn = mysql.connector.connect(
        host = db_config['host'],
        user = db_config['user'],
        password = db_config['password'],
        database = db_config['database']
    )
    cursor = conn.cursor()
    
    #Create a table if it does not exist 
    create_table_query = f"""
        CREATE TABLE IF NOT EXISTS PRICING_PLAN_FEATURES (
            pricing_plan_feature_id VARCHAR(255) PRIMARY KEY,
            app_id VARCHAR(255),
            feature VARCHAR(255)
                    )
    """
    
    cursor.execute(create_table_query)
    
    #Insert data into table 
    for index, row in df.iterrows():
        insert_query = f"""
        INSERT INTO APPS (pricing_plan_feature_id, app_id, feature)
        VALUES (%s,%s,%s)
        """
        cursor.execute(insert_query, (row['pricing_plan_feature_id'],row['app_id'],row['feature']))
        
    #Commit the transaction
    conn.commit()
    
    # Close the cursor and connection
    cursor.close()
    conn.close()      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    df_apps = pd.read_excel('./data/apps.xlsx')
    #print(df.columns)
    #Database configuration
    db_config = {
        'host' : 'localhost',
        'user' : 'root',
        'password': '12345678',
        'database': 'Apps'
    }
    df_apps.dropna(inplace=True)
    #Load data to MySQL
    load_apps_table(df_apps,db_config)
    print('Loading Apps Table is complete')
    
    df_reviews  = pd.read_csv('./data/reviews.csv')
    load_reviews_table(df_reviews,db_config)
    print('Loading Reviews Table is completed')
    
    df_pricing_plans = pd.read_csv('./data/pricing_plans.csv')
    load_pricing_plans_table(df_pricing_plans,db_config)
    print('Loading Pricing Plans Table is completed')
    
    df_key_benefits = pd.read_excel('./data/key_benefits.xlsx')
    load_key_benefits_table(df_key_benefits, db_config)
    print('Loading Key Benefits Table is completed')
    
    df_apps_categories = pd.read_csv('./data/apps_categories.csv')
    load_apps_categories_table(df_apps_categories, db_config)
    print('Loading Apps Categories Table is completed')
    
    df_categories = pd.read_csv('./data/categories.csv')
    load_categories_table(df_categories,db_config)
    print('Loading Categories Table is complete')
    
    df_pricing_plan_features = pd.read_csv('./data/pricing_plan_features.csv')
    load_pricing_plan_features_table(df_pricing_plan_features,db_config)
    print('Loading Pricing Plan Feature Table is completed')