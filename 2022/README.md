# 2022

This year, I have decided that I'll be trying out these languages:
- Go
- Python
- Shell
- Gleam
- Elixir

Unfortunately, I **do not** plan to continue for the whole month. I'll come back and solve the remaining questions.

## Setup

I've added a `Makefile` for testing out stuff nicely.

<hr>

### Go

From the root directory: (`./2022`)

```
make go
```

(runs the entire suite: build, run and test)

<hr>

From the Go directory: (`./2022/src/go`)

- Build + Run (`make build`)
- Test (`make test`)
- Build + Run a single file (`make build-single`)
- Test a single file (`make test-single`)
- Lint a single file (`make lint-single`)
- Run a "pipeline" on a single file (`make pipeline`)
- Run the entire suite (`make batch`)

<hr>
