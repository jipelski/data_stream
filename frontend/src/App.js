import logo from './logo.svg';
import './App.css';
import DataForm from './components/DataForm';


function App() {
  return (
    <div className="App">
      <header className="App-header">
          <h1>Sensor Data Query</h1>
          <DataForm />
      </header>
    </div>
  );
}

export default App;
