import UploadDataset from "./components/UploadDataset";
import DatasetList from "./components/DatasetList";

function App() {
  return (
    <div style={{padding: "24px"}}>
      <h1>AI Dataset Platform</h1>
      <UploadDataset />
      <hr />
      <DatasetList />
    </div>
  )
};

export default App;
