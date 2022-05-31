## GraphQl with Python FastAPI
Need to make a  python environment to install all of the required packages to run graphql and fast-api. We will use Orator ORM for the db chores.

## Technologies
* Python
* Fast API
* Graph-QL
* Orator
* psycopg2

```
# Making conda environment
conda create -n graphql python=3.9

# Activating environment
conda activate graphql

# installing packages seperatly
pip install graphene
pip install fastapi
pip install "uvicorn[standard]"
pip install 'strawberry-graphql[fastapi]'
pip install orator
pip install psycopg2-binary
```
Strawberry  is a new GraphQL library for Python 3, inspired by dataclasses.


# Story:
Why GraphQL?
(And why GraphQL over traditional REST?)

REST is the de-facto standard for building web APIs. With REST, you have multiple endpoints for each CRUD operation: GET, POST, PUT, DELETE. Data is gathered by accessing a number of endpoints.

For example, if you wanted to get a particular user's profile info along with their posts and relevant comments, you would need to call four different endpoints:

```
/users/<id> returns the initial user data
/users/<id>/posts returns all posts for a given user
/users/<post_id>/comments returns a list of comments per post
/users/<id>/comments returns a list of comments per user
```
This can result in request overfetching since you'll probably have to get much more data than you need.

Moreover, since one client may have much different needs than other clients, request overfetching and underfetching are common with REST.

GraphQL, meanwhile, is a query language for retrieving data from an API. Instead of having multiple endpoints, GraphQL is structured around a single endpoint whose return value is dependent on what the client wants instead of what the endpoint returns.

In GraphQL, you would structure a query like so to obtain a user's profile, posts, and comments:

```python
query {
  User(userId: 2){
    name
    posts {
      title
      comments {
        body
      }
    }
    comments {
      body
    }
  }
}
```
Voila! You get all the data in just one request with no overfetching since we specified exactly what we want.