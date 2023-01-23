import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Authors";
import axios from "axios";
import BookList from "./components/books";
import {HashRouter, Route, Link, Switch, Redirect} from "react-router-dom";
import AuthorBookList from "./components/AuthorBook";

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
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8080/api/authors')
            .then(response => {
                const authors = response.data
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
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
                                <Link to='/'>Authors</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <AuthorList authors={this.state.authors}/>}/>
                        <Route exact path='/books' component={() => <BookList items={this.state.books}/>}/>
                        <Route exact path='/author/:id' component={() => <AuthorBookList items={this.state.books}/>}/>
                        <Redirect from='/authors' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </HashRouter>
            </div>
        );
    }
}

export default App;
