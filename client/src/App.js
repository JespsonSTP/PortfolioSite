import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Home  from './pages/Home'
import {ApolloClient, InMemoryCache, ApolloProvider, HttpLink ,from} from '@apollo/client'
import {onError} from '@apollo/client/link/error'
import { AppContextProvider } from './context/AppContext';
import './App.css';

/*

my first query to get my projects

const GET_PROJECTS = gql`
                      query{
                        projects {
                          edges{
                            node{
                              id
                              projectname
                              textDescription
                            }
                          }
                        }
                      }
                    `;
*/

const errorLink = onError(({ graphqlErrors, networkError}) =>{
  if(graphqlErrors) {
    graphqlErrors.map(({message, location, path}) =>{
      alert(`Graphql error ${message}`)
    })
  }
})

const link = from([
  errorLink,
  new HttpLink({uri: 'http://127.0.0.1:8000/graphql/'})
])

//create an apollo client

const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: link,
})
/*
this is  my test to see if everything is connected 
and test the data i got back

client.query({
  query: GET_PROJECTS
}).then(res => console.log(res))
*/
function App() {
    return (
      <AppContextProvider>
      <ApolloProvider client={client}>
      <BrowserRouter>
      <Switch>
      <Route exact path="/" component={Home} />
      </Switch>
      </BrowserRouter>
    </ApolloProvider>
      </AppContextProvider>
    )
}

export default App