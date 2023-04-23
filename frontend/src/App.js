import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';

import { Users } from './components/Users';
import { About } from './components/about';

function App() {
  return (
    <Router>

      <div>
        <Switch>
          <Route path="/about" Component={About} />
          <Route path="/" Component={Users} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
