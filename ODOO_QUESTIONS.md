Below are detailed answers aligned with the current Odoo 19 documentation and present-day ecosystem practice. Some details may differ for older branches, but the basic mechanisms remain the same. ([Odoo][1])

1. **How is an Odoo module structured?**

A typical Odoo module is a Python package with `__manifest__.py` and `__init__.py`. Inside it, there are usually subdirectories organized by responsibility. There is no mandatory “hard” folder set, but the de facto structure is as follows: `models/` contains ORM models and business logic; `views/` contains XML definitions of forms, lists, search views, actions, and menus; `security/` contains access rights (`ir.model.access.csv`) and record rules; `data/` contains reference/service records, sequences, cron jobs, mail templates, and configuration; `demo/` contains demonstration data; `wizards/` or `wizard/` contains transient models and their views for wizards; `report/` contains reports; `controllers/` contains HTTP controllers; `static/` contains JS/CSS/images; and `tests/` contains tests. `__manifest__.py` describes the module metadata, dependencies, and lists of files to be loaded. ([Odoo][2])

It is important to understand that these are not just “folders for order.” Through the manifest, Odoo understands which XML/CSV files to load, in what order, which modules must be installed first, and which hooks to call. Therefore, an Odoo module is not only code, but a combination of Python, ORM definitions, XML views, security rules, and initialization data. ([Odoo][1])

2. **How are dependencies between modules implemented? How can you make one module installed together with another?**

Dependencies are defined in `__manifest__.py` through the `depends` field. This means that before installing the current module, Odoo must install the listed dependencies and load their models, fields, XML IDs, and extensions. If your module uses a model, view, security group, or field from another module, that module must be listed in `depends`. ([Odoo][1])

If one module must **always pull in another**, the most direct way is to specify it in `depends`. Then installing the current module will automatically install the dependency. But if we are talking about a “linking” module that should be installed only when two base modules are already installed, `auto_install` is usually used instead of a hard dependency alone. ([Odoo][1])

3. **What does `auto_install=True` do in manifest.py? When should it be used?**

`auto_install=True` tells Odoo that the module should be installed automatically if its dependency conditions are met. The classic scenario is a **link module** that integrates two other modules. For example, there is a Sales module and an Inventory module, while a third module only adds integration between them. In this case, the third module can be marked `auto_install=True`, and it will be installed automatically when its dependencies are installed. ([Odoo][1])

There is an important nuance: `auto_install` can be not only a boolean, but also a list. In that case, auto-installation happens when the modules from that list are already installed, while missing dependencies will also be pulled in. This is convenient for technical bridges, localizations, integration layers, and functionality that is not useful by itself but only as an addition to an existing stack. ([Odoo][1])

4. **What types of data are used in Odoo (`demo`, `data`)? What is the difference?**

A manifest usually contains two key file lists: `data` and `demo`. Files from `data` are loaded as regular module data: security, views, actions, menus, sequences, cron jobs, templates, base settings, reference data, and so on. These are “production” data required for the module to function. ([Odoo][1])

`demo` contains demonstration data. It is loaded only if the database/installation allows demo data (`--with-demo`) and is usually used for examples, training, test scenarios, and showcase data for Sales, Inventory, CRM, and similar modules. In production, it is usually not installed. In practice: `data` is required for functionality, while `demo` is only for examples and demo environments. ([Odoo][1])

5. **What does `noupdate="1"` mean? How does it affect module updates? Can such records be changed?**

In Odoo XML files, a `<data noupdate="1">` block means that records will be loaded during installation, but **will not be automatically overwritten** by XML data during subsequent module updates. This is needed for records that are expected to live their own life after installation: for example, access rights, settings, email templates, and cron jobs that an administrator may edit manually. ([Odoo][3])

At the same time, `noupdate` **does not make a record immutable**. It can still be changed through the ORM, UI, or SQL. The point is only that a module update will not overwrite its content from XML. If such a record still needs to be updated as part of module delivery, this is usually done through an upgrade script/migration rather than by relying on regular XML reloading. There are also service modes for reinitialization that affect noupdate records, but that is more of a development/upgrade tool than normal business practice. ([Odoo][3])

6. **QWeb uses `t-inherit-mode`. What modes exist and how do they differ?**

Modern QWeb has two main modes: `primary` and `extension`. `primary` creates a **new child template** that inherits from the original. In other words, you do not modify the parent template directly; instead, you build your own template on top of it. This is the correct approach when you need a separate resulting template based on a base one. ([Odoo][4])

`extension` works differently: it **modifies the parent template in place**. This mode is used for patching an existing template via XPath and similar mechanisms. It is applied when the task is not to create a new template, but to integrate into an existing screen, report, or snippet. A good interview answer is: `primary` means “create a new inherited template,” while `extension` means “modify the base template in place.” ([Odoo][4])

7. **The difference between `_inherit` and `_inherits`**

`_inherit` is **classic extension of an existing model**. You add fields, methods, constraints, and override behavior, but logically continue to work within the same model. Usually, it is the same business object, simply extended. For example, you add a field and a method to `res.partner`. This is the most common scenario. ([Odoo][2])

`_inherits` is **delegation**. Your model has its own table, but it stores references to one or more “parent” models through foreign keys, and the fields of the delegated model become transparently accessible as if they were its own. This is closer to composition than ordinary inheritance. It is used when you need a new business object with its own lifecycle and table, but you also want to reuse fields from another model without copying them. In short: `_inherit` means “I extend an existing model”; `_inherits` means “I build a new model on top of another through delegation.” ([Odoo][2])

8. **Why call `invalidate_cache()` after `cr.execute()`?**

Because the Odoo ORM aggressively caches recordset field values. If you perform `UPDATE`, `INSERT`, or `DELETE` directly through SQL, the ORM will not know about it automatically. As a result, within the same environment/request, it may continue returning old values from cache. You get “ghosts”: the database already contains new data, while the ORM still sees old data. ([Odoo][5])

This is critical after any **modifying** SQL operation (`CREATE`, `UPDATE`, `DELETE`). After such operations, the corresponding model/recordset cache must be invalidated. If the modified fields participate in dependencies of stored computed fields, cache invalidation alone is not enough: the ORM must also be told that the fields were modified so dependent computed fields can be recomputed. Otherwise, you may get inconsistency between the database, cache, and computed values. ([Odoo][5])

9. **What relational fields exist in Odoo? When should `Many2one`, `One2many`, and `Many2many` be used?**

The main relational fields are `Many2one`, `One2many`, and `Many2many`. `Many2one` is a reference to **one** record of another model. Classic examples: an order has one customer, an invoice has one company, and an order line belongs to one order. This is the “ordinary foreign key.” ([Odoo][5])

`One2many` is the reverse side of `Many2one`. It does not exist by itself: for a `One2many`, there must be a corresponding `Many2one` on the other model. This is convenient for cases like “an object has a set of child lines”: an order has order lines, a partner has contacts, and an invoice has lines. ([Odoo][6])

`Many2many` is used when both sides can contain many records: a product belongs to many tags, a user belongs to many groups, and a group contains many users. The practical rule is: `Many2one` is the main working foreign key; `One2many` is convenient for displaying and managing a set of child records; `Many2many` is used when you need a symmetric or nearly symmetric many-to-many relationship. ([Odoo][7])

10. **What is `NewID`? When does it appear?**

`NewID` is an internal ORM pseudo-identifier for a record that has **not yet been saved**. It is needed so that Odoo can work with “virtual” objects before the actual row is inserted into the database: in `onchange`, in `new()`, in temporary x2many lines in a form, and in other scenarios where a record already exists in memory as an ORM object but does not yet have a real PostgreSQL integer ID. Essentially, it is a marker meaning “this record already exists in the ORM context, but it has not yet been flushed/created in the database.” ([GitLab][8])

In practice, `NewID` most often appears during debugging, in `onchange` errors, in domains/logic for unsaved One2many lines, and when working with `record.new(vals)`. For an interview, it is enough to explain that it is a temporary pseudo-ID for an unsaved record. ([GitHub][9])

11. **The difference between `compute`, `inverse`, and `onchange`**

`compute` is a way to calculate a field value from other fields. The field is declared as computed, and the `compute` method assigns a value to it. If the field is stored, its value can be stored in the database and recomputed when dependencies change (`@api.depends`). ([Odoo][5])

`inverse` is needed for reverse writing: by default, a computed field is read-only, while `inverse` allows a user or code to write a value into the computed field, and the method then distributes that change back into the source data. In other words, `compute` calculates the field “forward,” while `inverse` decomposes the entered value “backward” into its dependencies. ([Odoo][5])

`onchange` is a completely different mechanism. It works at the form level in the web client: the user changes a field, Odoo calls a method and returns changes to the interface **without saving them to the database**. The documentation explicitly recommends not building critical business logic on `onchange`, because it does not run during ordinary programmatic `create/write`; it is tied to forms. In practice: `compute`/`inverse` are part of the model and its invariants; `onchange` is a UI convenience. ([Odoo][10])

12. **What does `check_company` do in relational fields?**

`check_company=True` on a relational field adds an automatic company consistency check. Odoo will ensure that the related record is valid from the perspective of the multi-company logic of the current record and active company. This protects against errors such as “a document from company A references a record from company B.” ([Odoo][5])

It should be used where an inter-model relationship must respect company boundaries: accounting, inventory, partners/journals/accounts, and documents with `company_id`. It is especially useful on `Many2one`, where the user manually selects a related record. It is not a replacement for all multi-company logic, but it is a very useful built-in guardrail. ([Odoo][5])

13. **If SQL was executed directly, what should be done so changes become visible to the ORM?**

The correct sequence is as follows. First, if the ORM may still have pending changes not yet written to the database, flush the corresponding fields/models. Then execute SQL. After modifying SQL, invalidate the cache of the affected model or recordset. If you changed fields that stored computed fields depend on, additionally notify the ORM via `modified(...)` so dependent fields are recomputed. ([Odoo][5])

A good interview answer is: “before raw SQL — flush; after raw SQL — invalidate cache; and when changing dependencies of computed fields — also call `modified()`/recompute.” `cr.execute()` by itself is not enough if you want to maintain ORM state consistency. ([Odoo][5])

14. **What is lazy loading in Odoo?**

In practical Odoo terminology, lazy loading means that record fields are not all read in advance. The ORM loads values **when they are first accessed**, and then keeps them in the environment cache. This reduces unnecessary queries and does not pull everything from the database “just in case.” ([Odoo][5])

But in Odoo, lazy loading is almost immediately combined with prefetching: as soon as you access a field of one record from a recordset, the ORM usually loads the same field and a set of simple stored fields for a wider recordset. Therefore, the practical answer is: lazy loading is deferred loading on first access, while prefetching is its optimization against N+1 queries. ([Odoo][5])

15. **How does `prefetch_fields` work and how does it affect performance?**

The basic mechanism is this: when you read a field on a record, the ORM does not limit itself to that single cell. It uses cache and prefetch heuristics: it loads fields for a wider recordset, and all simple stored fields from one table are often read with a single SQL query. This greatly reduces the number of queries and fights the N+1 problem. ([Odoo][5])

In practice, the context flag `prefetch_fields=False` is also used — it can be found in Odoo code — to disable or reduce this heuristic in special scenarios, for example during very large data passes where excessive prefetching inflates memory usage and pulls too much unnecessary data. Therefore, its effect on performance is twofold: **by default, prefetching usually speeds things up**, but in some heavy-duty cases it is weakened for better control over memory and extra reads. ([GitHub][11])

16. **What are mixins in Odoo? How do they work?**

Mixins in Odoo are reusable models/classes that add a shared set of capabilities to a group of models through inheritance. The documentation directly describes mixins as Odoo models that provide useful features through inheritance. The most typical examples are `mail.thread`, `mail.activity.mixin`, and `image.mixin`. ([Odoo][12])

They are used when you need to attach standard behavior without copy-paste: chatter, activities, images, UTM, portal functionality, rating, and so on. This is often combined with `_inherit`: you either build your own model and inherit a mixin, or extend an existing model and add mixin functionality to it. ([Odoo][12])

17. **How do dynamic reports differ from regular reports?**

The term “dynamic report” in Odoo is not always formalized in the same way, but “regular” reports usually mean classic QWeb reports: there is an `ir.actions.report`, a QWeb/HTML template, and, if a PDF is needed, rendering through wkhtmltopdf. This is a static document generated from a recordset and printed or downloaded. ([Odoo][13])

By “dynamic reports,” people more often mean interactive reports in the style of the accounting/reporting engine: the user changes filters, expands rows, drills down, and recalculates the view without generating a fixed printable document. In Odoo, this is often built on report engine models, lines, expressions, and client-side rendering. In other words, a regular report means “generate a document,” while a dynamic report means “provide an interactive analytical view.” ([Odoo][14])

18. **What is an abstract model?**

`AbstractModel` is a model without a full standalone data table, intended for shared APIs, shared logic, and reusable behavior. The documentation explicitly distinguishes `Model`, `TransientModel`, and `AbstractModel`, with `_auto=False` by default for abstract models. The idea is that an abstract model exists so other models can inherit from it, not so business users can create its records as a standalone object. ([Odoo][5])

It should be used for base classes, service layers, mixins, common methods, and shared contract APIs. If you do not need a standalone business object with its own lifecycle in the database, but only shared logic, an abstract model fits better than a regular model. ([Odoo][5])

19. **What is a transient model? What tasks is it intended for?**

`TransientModel` is a temporary model: it does have records in the database, but those records are considered temporary and are automatically cleaned up, or vacuumed, after some time. The documentation directly associates them with wizards. It is not “not saved at all,” but rather “saved temporarily and not treated as a long-term business object.” ([Odoo][5])

Typical tasks include action wizards, temporary forms, intermediate parameters, settings wizards, confirmations, and import steps. A very characteristic sign is that such records exist for a UI process/scenario, not as part of the company’s long-term domain data. ([Odoo][2])

20. **The difference between abstract and transient models**

`AbstractModel` is essentially a template/base for inheritance, usually without its own domain table. Its purpose is to provide shared code and interfaces. `TransientModel`, on the contrary, has real records in the database, but they are temporary and automatically cleaned up. ([Odoo][5])

So, briefly: abstract is for reusing logic; transient is for temporary process data. If you need a shared `do_something()` method for ten models — use abstract. If you need a wizard to “confirm an operation and select parameters” — use transient. ([Odoo][5])

21. **What are migrations in Odoo? When are they needed and how are they implemented?**

Migrations are code that brings an existing database and its data into alignment with a new module version. They are needed when models, fields, XML IDs, relationships, reference data, names, storage logic, or existing data transformations change. The documentation on custom database upgrades specifically highlights cases involving renaming models/fields/XML IDs and nuances around `noupdate` data. ([Odoo][15])

Migrations are implemented through upgrade scripts: Python files with a `migrate(cr, version)` function in a tree such as `$module/migrations/$version/` or `$module/upgrades/$version/`, with `pre`, `post`, and `end` phases. Inside them, SQL and ORM operations can be executed, and for complex upgrades, `odoo.upgrade.util` can be used. This is the correct tool for versioned transformations, not hooks. ([Odoo][16])

22. **What are hooks in Odoo? What types exist and where are they declared?**

Hooks are special module lifecycle functions declared in the manifest. In the current manifest documentation, `pre_init_hook`, `post_init_hook`, and `uninstall_hook` are listed. They are used for actions before initialization, after installation, and during module removal. ([Odoo][1])

They are declared in `__manifest__.py`, and the functions themselves must be available to the module through `__init__.py`. According to the current documentation, hooks receive `env`. Typical scenarios include one-time data initialization, complex environment preparation, and cleanup during uninstall. But for ordinary version updates and data transformations, migrations should be used instead of hooks. ([Odoo][1])

23. **How does a transaction work in Odoo? When do commit and rollback happen?**

The Odoo framework normally opens an SQL cursor/transaction for the duration of one RPC/API call. If execution succeeds, the transaction is committed. If an exception occurs, rollback is performed. The JSON-2 API documentation directly states that each call is executed in its own SQL transaction: success means commit, and error means discard/rollback. The coding guidelines also explicitly warn that manual commits should not be used without a very strong reason. ([Odoo][17])

The practical conclusion: write business operations so that an integral action fits into one call/transaction. Then there is less chance of ending up with partially applied changes. Some special scenarios — shell, cron, batch processing — may commit differently, but the base model is this: one request, one transaction. ([Odoo][18])

24. **How does a savepoint work? Where is it used and why?**

A `savepoint` is an internal partial rollback point inside an already open transaction. If a piece of code inside the savepoint fails, only that section can be rolled back without killing the whole outer transaction. This is convenient when you want to try a risky operation but do not want to lose everything else. ([Odoo][19])

In Odoo, savepoints are used both in the testing infrastructure (`SavepointCase`) and in application code around sections where a local error is acceptable. But they should not be abused: the coding guidelines separately warn that too many savepoints in one transaction hurt PostgreSQL performance. ([Odoo][19])

25. **What happens during simultaneous access to the same records? How does Odoo prevent race conditions?**

The main protection is not “Odoo magic,” but PostgreSQL’s transaction model plus proper organization of business methods. Different RPC/API calls run in different transactions, and if you split a critical business operation into several separate calls, concurrent changes can slip in between them. The JSON-2 documentation explicitly warns against such scenarios for reservations, payments, and similar cases. ([Odoo][17])

For critical sections, Odoo also uses row-locking patterns. In the cron documentation, you can see `try_lock_for_update()` with a repeated domain check after acquiring the lock. There are also API methods that combine actions into one transaction to avoid races between them; `search_read` is one example, where the documentation specifically says that it eliminates the race between separate `search` and `read` operations. A good engineering answer is: Odoo relies on database transactions, constraints, and row locks, while the developer must keep critical operations atomic. ([Odoo][20])

26. **How does `ensure_one()` work? When should it be used?**

`ensure_one()` checks that a recordset contains exactly one record. If there are 0 records or more than 1, the method raises an error. It is a protective mechanism for methods that semantically must work only on a singleton: opening the form of a specific document, building a URL for one record, processing one payment, printing one receipt. ([Odoo][5])

It is important not to overuse `ensure_one()`. Many Odoo ORM methods naturally work in batches, and forcibly reducing everything to a singleton harms performance and makes the code less “Odoo-way.” Use `ensure_one()` where the semantics are truly single-object, not merely because it was easier to write the method that way. ([Odoo][5])

27. **The difference between migrations and hooks**

Migrations are **versioned** data/schema transformations during module updates. They live in `migrations/` or `upgrades/`, are tied to a version, and run specifically during updates. This is the tool for evolving existing databases. ([Odoo][16])

Hooks are lifecycle points for module installation/removal, declared in the manifest. Their task is one-time actions around install/uninstall, not maintaining versioned changes across a chain of releases. Therefore, the rule is simple: if you are changing existing data between versions, use a migration; if you need a special action before/after installation or during uninstall, use a hook. ([Odoo][1])

28. **What is `queue_job` in Odoo? How does it work and why is it needed?**

`queue_job` is not part of core Odoo, but a popular OCA ecosystem module for asynchronous job queues. Its purpose is to defer execution of Odoo methods to the background so the user is not held inside an HTTP request and heavy work is not performed synchronously in the UI thread. OCA describes it as an integrated job queue / asynchronous jobs. ([GitHub][21])

It is needed for integrations, imports/exports, synchronizations, mass operations, long-running document generation, tasks with retry, and background processing. Architecturally, the idea is simple: a business method becomes a job, and the job runner picks it up and executes it separately, often with channels, retries, and status monitoring. In an interview, it is good to emphasize that this is the standard async tool in the Odoo ecosystem, but not part of the framework core. ([GitHub][21])

29. **How do you set a default value for a field?**

There are several ways. The most direct one is the `default=` attribute on the field: it can be a literal or a callable. The second important mechanism is `default_get()`, if the value depends on context, user, other fields, or complex initialization logic. The ORM documentation separately describes `default_get()` as the method for building default values. ([Odoo][5])

There are also defaults through context: keys such as `default_my_field` pass a default value when opening forms or creating records. The coding guidelines separately warn that such keys may unexpectedly “leak” further down the chain when other objects are created, unless the context is controlled. Another source is `ir.default`, which is used for user/company default values. ([Odoo][22])

30. **The difference between `@api.constrains` and `_sql_constraints`. Which fires first?**

`@api.constrains` works at the Python level. The method is called by the ORM on records where the specified fields were changed and must raise `ValidationError` if a business rule is violated. It is useful for complex checks, inter-field logic, and conditions that are inconvenient or impossible to express in pure SQL. ([Odoo][5])

`_sql_constraints` are database-level constraints. They are faster and more reliable for invariants such as `UNIQUE`, `CHECK`, simple non-negativity rules, and generally anything the database can express by itself. The documentation directly says that SQL constraints are usually more efficient than Python constraints and should be preferred when possible. ([Odoo][23])

As for which one fires “first,” it is better to answer carefully in an interview: **do not rely on order; rely on the responsibility of each layer**. A Python constraint lives in ORM logic, while an SQL constraint lives in PostgreSQL and is the final guarantee during the actual `INSERT/UPDATE`. Therefore, the practical rule is: anything that can be strictly and cheaply guaranteed at the database level should be kept in `_sql_constraints`; complex business validation should be kept in `@api.constrains`. ([Odoo][5])

[1]: https://www.odoo.com/documentation/19.0/developer/reference/backend/module.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/module.html"
[2]: https://www.odoo.com/documentation/19.0/developer/tutorials/backend.html "https://www.odoo.com/documentation/19.0/developer/tutorials/backend.html"
[3]: https://www.odoo.com/documentation/19.0/developer/reference/backend/data.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/data.html"
[4]: https://www.odoo.com/documentation/19.0/developer/reference/frontend/qweb.html "https://www.odoo.com/documentation/19.0/developer/reference/frontend/qweb.html"
[5]: https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/orm.html"
[6]: https://www.odoo.com/documentation/19.0/applications/studio/fields.html "https://www.odoo.com/documentation/19.0/applications/studio/fields.html"
[7]: https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/07_relations.html "https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/07_relations.html"
[8]: https://git.coopdevs.org/coopdevs/odoo/OCB/-/blob/19.0_2025-11-08/odoo/orm/identifiers.py "https://git.coopdevs.org/coopdevs/odoo/OCB/-/blob/19.0_2025-11-08/odoo/orm/identifiers.py"
[9]: https://github.com/odoo/odoo/issues/78501 "https://github.com/odoo/odoo/issues/78501"
[10]: https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/08_compute_onchange.html "https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/08_compute_onchange.html"
[11]: https://github.com/odoo/odoo/blob/19.0/addons/website_sale/controllers/main.py "https://github.com/odoo/odoo/blob/19.0/addons/website_sale/controllers/main.py"
[12]: https://www.odoo.com/documentation/19.0/developer/tutorials/mixins.html "https://www.odoo.com/documentation/19.0/developer/tutorials/mixins.html"
[13]: https://www.odoo.com/documentation/19.0/developer/reference/backend/reports.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/reports.html"
[14]: https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/customize.html "https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/customize.html"
[15]: https://www.odoo.com/documentation/19.0/developer/howtos/upgrade_custom_db.html "https://www.odoo.com/documentation/19.0/developer/howtos/upgrade_custom_db.html"
[16]: https://www.odoo.com/documentation/19.0/developer/reference/upgrades/upgrade_scripts.html?utm_source=chatgpt.com "Upgrade scripts — Odoo 19.0 documentation"
[17]: https://www.odoo.com/documentation/19.0/developer/reference/external_api.html "https://www.odoo.com/documentation/19.0/developer/reference/external_api.html"
[18]: https://www.odoo.com/documentation/19.0/developer/reference/cli.html "https://www.odoo.com/documentation/19.0/developer/reference/cli.html"
[19]: https://www.odoo.com/documentation/19.0/developer/reference/backend/testing.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/testing.html"
[20]: https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html "https://www.odoo.com/documentation/19.0/developer/reference/backend/actions.html"
[21]: https://github.com/oca/queue?utm_source=chatgpt.com "OCA/queue: Asynchronous Job Queue"
[22]: https://www.odoo.com/documentation/19.0/contributing/development/coding_guidelines.html "https://www.odoo.com/documentation/19.0/contributing/development/coding_guidelines.html"
[23]: https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/10_constraints.html "https://www.odoo.com/documentation/19.0/developer/tutorials/server_framework_101/10_constraints.html"
