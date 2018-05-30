# Music-Recommender
A music recommendation system using the Yahoo! music dataset

INTRODUCTION

The goal is to propose a music recommendation system based on user preference analysis. To do this, we analyze raw scores from the dataset. These consist of ratings for music items, which is given by the user. A recommender system is defined as a system that is able to find entities in a dataset that may be of interest to the user. In contrast to search engines, recommender systems do not base their results on a query, instead they rely on implicit and explicit connections between users and items, such as ratings or other past interactions.

Music has always been something that we all have enjoyed. With the advent of the Internet, music today is readily and easily available to stream. An undeniable fact is that there is plenty of music available and searching for what you might be interested in is like looking for fish in the ocean.
There are plenty of genres, albums, artists and ultimately songs that one can listen to. The question now becomes, how then do we figure out what we really need? Most services provide users with several options to listen to but never really care about what users really want and what they would like. These providers expose music to users in simple ways. Some providers classify music based on keywords such as name of the artist, or genre, and some offer music based on how many number of times it has been played. The problem with these methods is they don’t really take the user’s preference into consideration. Thus, users spend a lot of time trying to find music they might like and this can lead to a frustrating experience.
Users need a system, a model that helps them identify music that they are most likely to listen to and this can be done based on classifying what we already have. We need a model where each song is given a rating that is done by the user. With a dataset containing sufficient number of user ratings, we can build a model that will predict what the user might like.

DATASET

The dataset we used for this project is the Yahoo! Music dataset. This dataset has 62,551,438 ratings of 296,111 music items by 249,012 users.
The ratings are given to different type of items: genres, artists, albums and tracks all tied together with a known taxonomy. Each user and item has at least 20 ratings in the dataset (test and train sets combined). The train set includes ratings (scores between 0 and 100) to tracks, albums, artists and genres performed by Yahoo! Music users. For each user participating in the test set, six items are listed. All these items are tracks (not albums, artists or genres).

DESIGN AND IMPLEMENTATION

HIERARCHY SEARCH

Music is classified in hierarchical structure; a track belongs to an album, an album is related to an artist, an artist is related to one or more genres. We utilize this concept to make music recommendations to a user.
Our first approach considered the album and artist ratings only. For every track of each user in the test set, we performed hierarchy search by searching through the training sets for its album and artist ratings and calculated the average of each item.
Thereafter, the top three rated items are recommended and the other three are not recommended. Our accuracy rate using this approach was 0.8396. 

The second approach we took was to add the ratings of the genres to the results we obtained from the first approach described above, calculated its average and recommended the top three rated items.
We also implemented weighted versions of the approaches above and obtained improved accuracy rates. 

EXPANSION OF THE HIERARCHY SEARCH

Basically, the same concept as the above method is also employed here. As a result of the sparseness of our dataset, there is the need to base recommendations on similar items as the ratings for the specific item may be unavailable.

The implementation is as follows;

• For every track of each user in the test set, we check if the track is contained in any Album or not. We then we retrieve the album’s rating.
• Next, we check whether the album is owned by any Artist. We retrieve the artist rating and also the rating of any other album owned by the particular Artist (similar albums).
• We check whether the track belongs in any genre by the Artist. We retrieve its rating (if it exists) and the rating of all other genres by the artist (similar genres) and also the other artists in those genres (similar artists).
• We now calculated the averages of the ratings of the groups of similar albums, similar artists and similar genre and summed them up to make recommendations for each user. The three highest rated tracks are recommended. 
• We also weighted these four components in the track hierarchy to improve accuracy rates.

MATRIX FACTORIZATION

Collaborative Filtering is the most popular approach to build Recommendation System and has been successfully employed in many applications. The CF recommender system works by collecting user feedback in the form of ratings for items in a given domain [1]. The most common types of CF systems is user-based and item-based approaches. The key advantage of CF recommender system is that it does not rely on the machine analyzable contents and therefore it is capable of accurate recommendations. In CF, user who had similar choices in the past, will have similar choices in the future as well.

The Matrix Factorization (MF) plays an important role in the Collaborative Filtering recommender system. The Matrix Factorization techniques are usually more effective because they allow use to discover the latent features underlying the interactions between users and items. Matrix Factorization is simply a mathematical tool for playing around with matrices, and is therefore applicable in many domains where one would like to find out something hidden under the data.

The algorithm can be described as follows. Firstly, we have a set of U users, and a set of I items. Let R be the matrix of size |U| x |I| that contains all the ratings that the users have assigned to the items. Now the latent features would be discovered. Our task then, is to find two matrices, P (|U|x К) and Q (|I|x К) such that their product approximately equals to R is given by R ≈ P x 𝑄𝑇 = Ȓ In this way, the Matrix factorization models map both users and items to a joint latent factor space of dimensionality f, user-item interactions are modeled as inner products in that space. Accordingly, each item i is associated with a vector 𝑞𝑖 ϵ 𝑅𝑓 , and each user u is associated with a vector 𝑝𝑢 ∈ 𝑅𝑓 . For a given item i, the elements of 𝑞𝑖 measure the extent to which the item possesses those factors positive or negative. The resulting dot product 𝑞𝑖𝑇 𝑝𝑢 captures the interaction between user u and item i, the users’ overall interest in the item characteristics. This approximates user u’s rating of item i which is denoted by 𝑟𝑢𝑖 leading to the estimate 𝑟𝑢𝑖= 𝑞𝑖𝑇 𝑝𝑢 . To learn the factor vectors (𝑝𝑢 and 𝑞𝑖), the system minimizes the regularized squared error on the set of known ratings.

Here, К is the set of the (u, i) pairs for which 𝑟𝑢𝑖 is known the training set. The constant λ controls the extent of regularization and is usually determined by cross-validation.

In the course of this project, we discovered our training dataset is very sparse and thought to combat this disadvantage. We used the alternating least squares matrix factorization algorithm to predict missing data in the training set using a rank size of ten and ten iterations. The results obtained were used to implement the hierarchy search algorithm described earlier. 

TRACK SIMILARITY BASED ON HAMMING DISTANCE

We want to compare two feature vectors, to measure how different (or how similar) they are. We hope that similar patterns will behave in a similar way. In building a music recommender system for users, similar tracks feature vectors (derived from their hierarchical structure) might indicate tracks with similar ratings per user. The distance between two items depends on both the representation used by the feature vectors and on the distance measure used. If the feature vectors are binary (i.e., all elements are 0 or 1) then the Hamming distance is a possible distance measure.

The Hamming distance between two binary sequences of equal length is the number of positions for which the corresponding symbols are different. For example the Hamming Distance between 10101010 and 11101001 is 3. In our case, each binary number used in the example represents the ID of features of the track such s album, artist and genre.

In the implementation of this algorithm, we considered tracks with five matching features as similar and therefore gave the same ratings. First we take a track for a user in the test dataset and then compare it with another track for the same user in the training set. The comparison is as follows;
• For track in the test dataset, we retrieve the album, artists and genre IDs
• For tracks in the training set, we also retrieve the same three features
• If five or more of the feature IDs of both tracks match, we consider them to be a match
• We retrieve the track rating of the matched training item and predict the same score for the testing item.

CONTENT FILTERING WITH DECISION TREE

For this, we utilize the “re_trainData2.txt” file. The first task is feature extraction for each user-item pair using the hierarchical information. Our next step is to create four sets of features for related tracks, albums, artists and genres.
Given any track, we use taxonomy to find related tracks from the same album. Next, using the user’s known ratings, we extract all existing related track ratings. We now create four features from the vector of related track ratings and these – minimum, maximum, average and number of ratings. Next, we generate four features based on related albums. This is done by extracting the four features using related albums by the same artist and we generate two sets of four features since there might be more than one genre associated with a track. These two sets of features come from related artists from the union of set of genres and from the union of set of genres respectively. We also extract album and artist scores and the associated label for these features in addition to the 16 features extracted.

ENSEMBLE 

An ensemble is defined as all the parts of a thing taken together, so that each part is considered only in relation to the whole. To implement an ensemble we create matrix 𝑅 of xxx rows and xxx columns. The results of each implemented algorithm represents a column 𝑅𝑛. We also have a column vector S containing the accuracy rates of each result used in the matrix 𝑆1,𝑆2,….𝑆𝑛 The aim is to find coefficients 𝑎1,𝑎2,…𝑎𝑛 ε𝑎 to linearly apply to our matrix that bests approximates the true solution.
The formula for coefficients is 𝑎=(𝑅𝑇𝑅)−1𝑅𝑇[(2𝑆−1)∗𝑡𝑜𝑡𝑎𝑙 𝑡𝑒𝑠𝑡𝑠𝑒𝑡] Upon finding coefficients, we then take linear combination of coefficients and results to derive an approximate best solution. 𝑅𝑏𝑒𝑠𝑡= 𝑅∗𝑎
