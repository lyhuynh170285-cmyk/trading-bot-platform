# Security Notes

## Security Concerns

### Dynamic Strategy Loading (eval usage)

**Location:** `model/signal_generation/_signal_generation.py:73`

The code uses `eval()` to dynamically load strategy classes:

```python
strategy_obj = eval(strategy["name"])(**strategy["params"], **extra_args)
```

**Risk:** This could allow code injection if strategy names are not properly validated.

**Recommendation:** 
- Consider using a strategy registry/mapping instead of `eval()`
- Ensure strategy names are validated against a whitelist of allowed strategy classes
- Use `getattr()` with a module reference instead of `eval()` for safer dynamic loading

**Example safer approach:**
```python
from model.strategies import STRATEGY_REGISTRY

strategy_class = STRATEGY_REGISTRY.get(strategy["name"])
if strategy_class is None:
    raise StrategyInvalid(strategy["name"])
strategy_obj = strategy_class(**strategy["params"], **extra_args)
```

## Good Security Practices Found

- API keys are loaded from environment variables, not hardcoded
- No hardcoded credentials found in the codebase
- Proper use of environment variables for sensitive configuration

