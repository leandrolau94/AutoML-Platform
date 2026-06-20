import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import DatasetDetailPage from "./pages/DatasetDetailPage";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={<HomePage />}
        />

        <Route
          path="/datasets/:id"
          element={<DatasetDetailPage />}
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App