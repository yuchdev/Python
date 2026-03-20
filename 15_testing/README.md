# Chapter 15. Testing

This chapter introduces testing foundations and practical tools in Python, focusing on unit tests, fixtures, and property-based thinking.

### Goals

- Write basic tests and assertions; structure testable code
- Use unittest for test cases, fixtures, and assertions
- Understand test isolation, setup/teardown, and dependency injection basics
- Explore property-based tests and invariants

### Theory (as in Python docs)

- Why test? The pyramid concept; fast feedback
- unittest framework
  - TestCase, subTest, setUp/tearDown, setUpClass/tearDownClass
  - Skipping, expected failures
- Assertions
  - assertEqual, assertTrue/False, assertRaises, custom messages
- Fixtures and isolation
  - Temporary files/dirs, environment variables; mocking note
- Property-based approach
  - Deterministic invariants; shrinking idea (intro)
