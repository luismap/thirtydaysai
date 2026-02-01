# 30 days ai challenge

Repository to follow the [30 days ai challenge](https://github.com/streamlit/30DaysOfAI)
using streamlit and snowflake

# references
* eval guide optimizations of llm judge [link](https://www.snowflake.com/en/engineering-blog/eval-guided-optimization-llm-judges-rag-triad/)
* ai observability [link](https://docs.snowflake.com/en/user-guide/snowflake-cortex/ai-observability)
* getting started with ai observability [link](https://github.com/Snowflake-Labs/sfguide-getting-started-with-ai-observability)
* cortex agents [link](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents)
* cortex analyst [link](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst)
* cortext agent REST API [link](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents-rest-api)


# when doing rag with snowflake and trulens keep in mind.

```txt
trulens-core>=1.0.0
trulens-connectors-snowflake>=1.0.0
trulens-providers-cortex>=1.0.0
snowflake-snowpark-python>=1.18.0,<2.0
pandas>=1.5.0
```

* trulens breakdown
    * trulens-core - Core TruLens functionality (TruSession, @instrument decorator)
    * trulens-connectors-snowflake - Snowflake connector for storing evaluation results
    * trulens-providers-cortex - Cortex LLM provider for evaluation metrics
    * pandas - Required for DataFrame operations with test datasets

* trulens requires stage in snowflake
```sql
CREATE STAGE TRULENS_STAGE
    DIRECTORY = ( ENABLE = true )
    ENCRYPTION = ( TYPE = 'SNOWFLAKE_SSE' );
```
# production tips for rag and monitoring

* Store evaluation results for historical analysis
* Set up alerts for quality degradation
* Run evaluations on a schedule (e.g., daily)
* Include production queries in your test set
* Compare metrics across app versions
* Use evaluation results to prioritize improvements

