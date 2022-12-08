from Load_data import load_data
import pandas as pd
import data_vizualization as vz
import Pivot_table as pt

if __name__ == "__main__":
    # load main data
    columns_name = ["user_id", "item_id", "rating", "timestamp"]
    data = load_data("DataSet/u.data", sep='\t', column_name=columns_name)
    print(data.head())
    
    # load movie_title
    movie_title = load_data("DataSet/Movie_Id_Titles")
    print(movie_title.head())
    
    # merge both data
    df = pd.merge(data, movie_title, on="item_id")
    
    # reading first five row
    print(df.head())
    df.groupby("title")["rating"].mean().sort_values(ascending=False).head()
    df.groupby("title")["rating"].count().sort_values(ascending=False).head()
    
    # creating rating dataframe
    rating=pd.DataFrame(df.groupby("title")["rating"].mean())
    rating["no_of_rating"]=pd.DataFrame(df.groupby("title")["rating"].count())
    
    # plot histogram
    vz.histogram(rating,"no_of_rating",bins=70)
    vz.histogram(rating,"rating",bins=70)
    
    # plot jointplot
    vz.jointplot(data=rating,x="rating",y="no_of_rating")
    
    # head of merge_data
    df.head()
    
    # pivot table
    movimat=pt.pivot_table(df,"user_id",column="title",value="rating")
    
    #################################################################
    print(rating.sort_values("no_of_rating",ascending=False).head())
    starwars_user_rating=movimat["Star Wars (1977)"]
    contact=movimat["Contact (1997)"]
    
    
    # correlation 
    similar_to_star_war_=movimat.corrwith(starwars_user_rating)
    print(similar_to_star_war_.head())
    similar_to_contact=movimat.corrwith(contact)
    print(similar_to_contact.head())
    corr_contact=pd.DataFrame(similar_to_contact,columns=["Correlation"])
    corr_contact.dropna(inplace=True)
    print(corr_contact.sort_values("Correlation",ascending=False).head())   
    corr_contact=corr_contact.join(rating["no_of_rating"])
    print(corr_contact.head())
    corr_contact=corr_contact[corr_contact["no_of_rating"]>100].sort_values("Correlation",ascending=False).head()
    print(corr_contact.head())
    corr_star_wars=pd.DataFrame(similar_to_star_war_,columns=["Correlation"])
    print(corr_star_wars.head())
    print(corr_star_wars[corr_star_wars["no_of_rating"]>200].sort_values("Correlation",ascending=False).head())