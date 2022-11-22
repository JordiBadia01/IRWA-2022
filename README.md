The code is created to be executed in a python environment. It has been created in a jupyter notebook, so libraries
won't have any problem when are imported. 

The code is structured in sequential cells which properly do its purposes starting by: 
1.Importing nltk package 
2.Importing other packages 
3. Reading the document of tweets 
4.Reading the csv of mapping 
5.The function of cleaning text 
6.the create index simple 
7.The creation of the index 
8. You can introduce in index['term here'] the term you are interesed in finding 
9. Simple function of search 
10.Query search will ask you to input a term 
11.the function create inverted index with normalized term frequency and inverse document frequency 
12. Generates the inverted index
13. The function rank the documents
14. Function search
15. Complementary function listing hashtags
16. Function tweet displayer
17. You can insert a query which will display the tweets relevant information in the order of the ranked documents.

Everything is implemented to being executed cell per cell.

In the Evaluation Part is the same procedure, you must have the documents in the folder of the file to upload it. The rest is set to be executed sequentially, first the queries, then the upload of the file, the evaluation functions and finally there is the T-SNE PLOT, here is probably that the user have to install gensim library.

In the part 3, we follow the same procedure as the previous parts, we must have the documents inside the same folder as the script. Once all the data is uploaded, it is only necessary to execute cell per cell and once the inverted index is created, then the different ranking functions are executed and post the ranking of the proposed queries.

That's all, any doubt send a mail to jordi.badia01@estudiant.upf.edu or to nil.agell01@estudiant.upf.edu
