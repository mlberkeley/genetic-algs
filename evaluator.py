
import sympy as sy

class Evaluator(object):
    @staticmethod
    def score(node, data, node_var):
        """ Score function

            Args:
                node: Node object
                data: Data object
                node_var: label for symbol corresponding to what variable
                          the tree represents  # TODO better name

            Returns:
                float
        """
        # Collapse tree into function
        func = node.collapse()

        # Evaluate function
        times = data.times()

        best_error = 9999999999
        for y in data.variables():
            if node_var == y:
                continue

            # Compute ansatz partial derivative
            dxdy = func.diff(sy.Symbol(y))

            residuals = 0
            for i, t in enumerate(times[:-1]):
                delx = data.get(node_var)[i+1] - data.get(node_var)[i]
                dely = data.get(y)[i+1] - data.get(y)[i]
                residual = dxdy(t) - delx / dely
                residuals += np.log(1 + abs(residual))
            residuals *= -1.0 / len(times)

            if residuals < best_error:
                best_error = residuals

       return best_error
        

    @staticmethod
    def evaluate(node, data, time):
        # TODO not sure if useful
        return node.func(*[Evaluator.evaluate(child, data, time)
                           for child in node.children])
