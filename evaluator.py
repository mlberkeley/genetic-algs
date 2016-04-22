
import numpy as np
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

        worst_error = 9999999999
        for y in data.variables():
            if node_var == y:
                continue

            # Compute ansatz partial derivative
            dxdy = func.diff(sy.Symbol(y))

            residuals = 0
            t_sym = sy.Symbol("t")
            for i, t in enumerate(times[:-1]):
                delx = data.get(node_var)[i+1] - data.get(node_var)[i]
                dely = data.get(y)[i+1] - data.get(y)[i]
                residual = float(dxdy.subs(t_sym, t) - delx / dely)
                residuals += np.log(1 + abs(residual))
            residuals *= -1.0 / len(times)

            if residuals < worst_error:
                worst_error = residuals

        return worst_error
