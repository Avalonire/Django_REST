import logo from './logo.svg';
import './App.css';
import React from "react";
import AuthorList from "./components/Authors";
import axios from "axios";

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    // componentDidMount() {
    //     const authors = [
    //         {
    //             'first_name': 'James',
    //             'last_name': 'Byron',
    //             'birthday_year': '1834',
    //         },
    //         {
    //             'first_name': 'Alexander',
    //             'last_name': 'Grin',
    //             'birthday_year': '1880',
    //         },
    //     ]
    //     // изменение state на наши компоненты встроенной функцией
    //     this.setState(
    //         {
    //             'authors': authors
    //         }
    //     )
    // }

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
            <div>
                <AuthorList authors={this.state.authors}/>
            </div>
        );
    }
}

export default App;
