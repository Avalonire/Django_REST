import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Authors";
import axios from "axios";
import BookList from "./components/books";
import {HashRouter, Route, Link, Switch, Redirect} from "react-router-dom";
import AuthorBookList from "./components/AuthorBook";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie/es6";

const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>
                Page on address '{location.pathname}' not found
            </h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'books': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        // localStorage.setItem('token', token)
        this.setState({'token': token}, () => this.load_data())
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        // const token = localStorage.getItem('token')
        this.setState({'token': token}, () => this.load_data())
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8080/api-token-auth/', {username: login, password: password})
            .then(response => {
                this.set_token(response.data['token'])
            }).catch(error => alert('Wrong Password!'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'aplication/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token' + this.state.token
        }
        return headers
    }

    load_data() {
        axios.get('http://127.0.0.1:8080/api/authors', {headers})
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors['results']
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8080/api/books', {headers})
            .then(response => {
                const books = response.data
                this.setState(
                    {
                        'books': books['results']
                    }
                )
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
    }


    render() {
        return (
            <div className='App'>
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/books'>Books</Link>
                            </li>
                            <li>
                                {this.is_authenticated() ?
                                    <button onClick={() => this.logout()}>
                                        Logout
                                    </button> :
                                    <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList items={this.state.books}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorBookList items={this.state.books}/>}/>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(login, password) => this.get_token(login, password)}/>}/>
                    </Switch>
                </HashRouter>
            </div>
        );
    }
}

export default App;
