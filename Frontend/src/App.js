import logo from './logo.svg';
import './App.css';

const API_BackPORT = process.env.REACT_APP_BackendPORT

console.log(API_BackPORT)

const App = () => {

  return (
    <main>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    </main>
  );
}

export default App;
