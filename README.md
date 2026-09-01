<div align="center">

<!-- Header Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&custom_color_list=0,2,2,5,30&height=210&section=header&text=Debaditya%20Hait&fontSize=42&fontColor=ffffff&animation=fadeIn&subtext=AI%20Systems%20%E2%80%A2%20Distributed%20Runtimes%20%E2%80%A2%20Open%20Source%20Contributor&subfontSize=15&subfontColor=abb2bf" width="100%" alt="Debaditya Hait Banner" />

<!-- Dynamic Animated Typing Subtitle -->
<a href="https://github.com/debadityahait">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=18&pause=1000&color=58A6FF&center=true&vCenter=true&width=750&lines=Contributor+to+TensorFlow%2C+PyTorch%2C+pnpm%2C+Vite%2C+Deno%2C+Redis;AI+Systems+Architect+%E2%80%A2+Distributed+Storage+%E2%80%A2+Edge+Inference;Ex-Samsung+PRISM+Research+Intern+%E2%80%A2+IIT+Madras+Research;LeetCode+Guardian+(Top+2%25)+%E2%80%A2+Codeforces+Expert;9x+Microsoft+Certified+%E2%80%A2+Claude+Certified+Architect" alt="Typing SVG" />
</a>

<br/>

<!-- Social & Verification Badges -->
<p align="center">
  <a href="https://linkedin.com/in/debadityahait" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:debaditya2005hait@gmail.com">
    <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
  <a href="https://leetcode.com/u/debadityahait/" target="_blank">
    <img src="https://img.shields.io/badge/LeetCode-Guardian%20(Top%202%25)-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" alt="LeetCode Guardian" />
  </a>
  <a href="https://codeforces.com/profile/debadityahait" target="_blank">
    <img src="https://img.shields.io/badge/Codeforces-Expert-1F8ACB?style=for-the-badge&logo=codeforces&logoColor=white" alt="Codeforces Expert" />
  </a>
  <a href="#certifications">
    <img src="https://img.shields.io/badge/Microsoft-9x%20Certified-0078D4?style=for-the-badge&logo=microsoft&logoColor=white" alt="9x Microsoft Certified" />
  </a>
  <a href="#certifications">
    <img src="https://img.shields.io/badge/Anthropic-Claude%20Architect-D97706?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Certified Architect" />
  </a>
</p>

</div>

---

### Overview

Computer Science Engineering student focused on **AI systems architecture, edge-native inference optimization, and distributed storage runtimes**. Active open-source contributor across major ecosystems including **Google TensorFlow, PyTorch, Rust-native pnpm, Vite, Deno, AWS Lambda, Node Redis, CERN TIGRE, and Cloudflare**.

Previous research includes internships at **Samsung R&D Institute India** (lightweight encoder-only guardrails for AI safety, ModernBERT-large 35ms inference) and **IIT Madras** (Physics-Informed Neural Networks for Alzheimer's progression modeling). Holds **9x Microsoft Certifications**, **Claude Certified Architect**, and ranks in the **Top 2% on LeetCode (Guardian)**.

---

<!-- Quick Stat Grid -->
<div align="center">

| Open Source PRs | Merged Upstream | Competitive Rating | Certifications | Education |
| :---: | :---: | :---: | :---: | :---: |
| **56 Pull Requests**<br/>*(52 Unique Codebases)* | **17 Merged PRs**<br/>*(TensorFlow, PyTorch, pnpm, Vite)* | **LeetCode Guardian** (Top 2%)<br/>**Codeforces Expert** | **9x Microsoft Certified**<br/>**Claude Certified Architect** | **BTech CSE @ SRMIST** (8.5)<br/>**BS Data Science @ IIT Madras** |

</div>

---

## Open Source Contributions

Summary: **56 pull requests across 52 unique repositories** (17 merged upstream, 27 active open) across **Rust, C/C++, Python, Go, and TypeScript**.

<div align="center">
  <img src="https://img.shields.io/badge/Total%20PRs-56-0969da?style=for-the-badge&logo=github&logoColor=white" alt="Total PRs" />
  <img src="https://img.shields.io/badge/Merged%20Upstream-17-238636?style=for-the-badge&logo=git&logoColor=white" alt="Merged PRs" />
  <img src="https://img.shields.io/badge/Active%20Open-27-8957e5?style=for-the-badge&logo=githubactions&logoColor=white" alt="Open PRs" />
  <img src="https://img.shields.io/badge/Stack-Rust%20%7C%20C%2B%2B%20%7C%20Python%20%7C%20Go%20%7C%20TS-d97706?style=for-the-badge" alt="Languages" />
</div>

<br/>

### Merged Upstream Pull Requests

<table>
  <thead>
    <tr>
      <th width="28%">Repository</th>
      <th width="14%">Pull Request</th>
      <th width="14%">Stack / Diff</th>
      <th width="44%">Technical Solution & Impact</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <b>Rust-Native pnpm Engine</b><br/>
        <code>pnpm/pnpm</code>
      </td>
      <td>
        <a href="https://github.com/pnpm/pnpm/pull/13059"><b>#13059</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Rust-dea584?style=flat-square&logo=rust&logoColor=black"/><br/>
        <code>+1,033 / -125</code>
      </td>
      <td>
        <b>Git Resolver Manifest Reader & Security Hardening:</b> Implemented a resolve-time archive fetch and manifest reader in Rust (<code>GitResolver</code>) for <code>pacquet</code>, fixing a lockfile generation panic during git-hosted dependency installs. Patched option-injection vulnerability in <code>git clone</code> (<code>--upload-pack</code>) and prevented subpath directory traversals (<code>#path:/../..</code>) across 5 crates.
      </td>
    </tr>
    <tr>
      <td>
        <b>Rust-Native pnpm Engine</b><br/>
        <code>pnpm/pnpm</code>
      </td>
      <td>
        <a href="https://github.com/pnpm/pnpm/pull/13056"><b>#13056</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Rust-dea584?style=flat-square&logo=rust&logoColor=black"/><br/>
        <code>+260 / -12</code>
      </td>
      <td>
        <b>Git Specifier Normalization:</b> Developed a cycle-safe Git specifier normalization module in Rust, preventing false-stale lockfile errors on equivalent protocols (<code>git+https://</code> vs <code>git://</code>) and hosted shortcuts (<code>github:</code>) during frozen installs.
      </td>
    </tr>
    <tr>
      <td>
        <b>Google TensorFlow Core</b><br/>
        <code>tensorflow/tensorflow</code>
      </td>
      <td>
        <a href="https://github.com/tensorflow/tensorflow/pull/124961"><b>#124961</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white"/><br/>
        <code>+28 / -9</code>
      </td>
      <td>
        <b>oneDNN Layout Rewriting Crash Fix:</b> Preserved 64-bit integer convolution attributes across oneDNN layout rewriting passes in TensorFlow's C++ kernel engine, converting fatal process aborts into clean <code>InvalidArgumentError</code> exceptions.
      </td>
    </tr>
    <tr>
      <td>
        <b>PyTorch Distributed Core</b><br/>
        <code>pytorch/pytorch</code>
      </td>
      <td>
        <a href="https://github.com/pytorch/pytorch/pull/191831"><b>#191831</b></a><br/>
        <a href="https://github.com/pytorch/pytorch/commit/30731ee8f01763cf1d32dc2e3962f51fc034c482"><code>30731ee</code></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/><br/>
        <code>+4 / -2</code>
      </td>
      <td>
        <b>Symmetric-Memory Triton Hooks:</b> Resolved Ruff B018 static analysis warnings in <code>torch.distributed._symmetric_memory</code> while preserving deliberate lazy module attribute lookup mechanics across NVSHMEM and Shared Memory Triton utilities.
      </td>
    </tr>
    <tr>
      <td>
        <b>Vite Build Engine</b><br/>
        <code>vitejs/vite</code>
      </td>
      <td>
        <a href="https://github.com/vitejs/vite/pull/22947"><b>#22947</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/><br/>
        <code>+100 / -2</code>
      </td>
      <td>
        <b>Chunk Import Map CSS Caching:</b> Fixed browser cache collisions in Vite's experimental chunk import-map engine by mapping dynamically extracted CSS assets back to parent Rollup chunks and generating stable Web Import Map specifiers.
      </td>
    </tr>
    <tr>
      <td>
        <b>PostHog CLI</b><br/>
        <code>PostHog/posthog</code>
      </td>
      <td>
        <a href="https://github.com/PostHog/posthog/pull/70314"><b>#70314</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Rust-dea584?style=flat-square&logo=rust&logoColor=black"/><br/>
        <code>+248 / -30</code>
      </td>
      <td>
        <b>Sourcemap Upload Concurrency:</b> Replaced a hardcoded global Rayon thread pool with an isolated, configurable concurrency pool in the Rust PostHog CLI, exposing <code>--concurrency</code> controls to prevent CI/CD network and resource exhaustion.
      </td>
    </tr>
    <tr>
      <td>
        <b>Node Redis</b><br/>
        <code>redis/node-redis</code>
      </td>
      <td>
        <a href="https://github.com/redis/node-redis/pull/3388"><b>#3388</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/><br/>
        <code>+66 / -8</code>
      </td>
      <td>
        <b>Sentinel Outage Retry Bounding:</b> Enforced <code>maxCommandRediscovers</code> bounds on post-connect Sentinel topology rediscoveries during cluster outages and implemented <code>#resetInBackground()</code> for graceful promise rejections.
      </td>
    </tr>
    <tr>
      <td>
        <b>rclone Cloud Sync</b><br/>
        <code>rclone/rclone</code>
      </td>
      <td>
        <a href="https://github.com/rclone/rclone/pull/9712"><b>#9712</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white"/><br/>
        <code>+100 / -55</code>
      </td>
      <td>
        <b>Context-Aware SDK Calls:</b> Refactored Dropbox backend to propagate caller <code>context.Context</code> down to HTTP execution sites, eliminating leaked goroutines and ensuring prompt cancellation during interrupted transfers.
      </td>
    </tr>
    <tr>
      <td>
        <b>CERN TIGRE</b><br/>
        <code>CERN/TIGRE</code>
      </td>
      <td>
        <a href="https://github.com/CERN/TIGRE/pull/762"><b>#762</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/MATLAB-e16737?style=flat-square"/><br/>
        <code>+18 / -2</code>
      </td>
      <td>
        <b>Tomography Calibration Math:</b> Corrected Varian CBCT rotational scan direction math (CW vs CC) and uncompressed XIM pixel buffer decoding in CERN's TIGRE reconstruction toolbox, verified against Zenodo phantom datasets.
      </td>
    </tr>
    <tr>
      <td>
        <b>Deepset Haystack AI</b><br/>
        <code>deepset-ai/haystack-core-integrations</code>
      </td>
      <td>
        <a href="https://github.com/deepset-ai/haystack-core-integrations/pull/3543"><b>#3543</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/><br/>
        <code>+141 / -3</code>
      </td>
      <td>
        <b>SentenceTransformers Quantization:</b> Resolved divide-by-zero errors in single-text int8/uint8 embeddings by introducing static pre-calibrated quantization ranges (<code>shape: (2, D)</code>).
      </td>
    </tr>
    <tr>
      <td>
        <b>IBM / DS3 Docling</b><br/>
        <code>docling-project/docling</code>
      </td>
      <td>
        <a href="https://github.com/docling-project/docling/pull/3875"><b>#3875</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/><br/>
        <code>+45 / -2</code>
      </td>
      <td>
        <b>Document Pipeline Crash Fix:</b> Added defensive page validation in <code>SimplePipeline</code> to skip image enrichment for PPTX native charts without page renders, fixing an index out-of-bounds conversion crash.
      </td>
    </tr>
    <tr>
      <td>
        <b>Neovim Core</b><br/>
        <code>neovim/neovim</code>
      </td>
      <td>
        <a href="https://github.com/neovim/neovim/pull/41067"><b>#41067</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black"/> <img src="https://img.shields.io/badge/Lua-2C2D72?style=flat-square&logo=lua&logoColor=white"/><br/>
        <code>+22 / -2</code>
      </td>
      <td>
        <b>UI2 Highlight Retention:</b> Engineered buffer-scoped highlight lifecycle checks in Neovim's C command-line UI subsystem to preserve substitution confirmation highlights under <code>nohlsearch</code>.
      </td>
    </tr>
    <tr>
      <td>
        <b>Twenty CRM</b><br/>
        <code>twentyhq/twenty</code>
      </td>
      <td>
        <a href="https://github.com/twentyhq/twenty/pull/23945"><b>#23945</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/><br/>
        <code>+80 / -2</code>
      </td>
      <td>
        <b>Relational Data Preservation:</b> Patched entity deduplication in NestJS/GraphQL backend services, preserving polymorphic relations and timeline activity records during contact merges.
      </td>
    </tr>
    <tr>
      <td>
        <b>AWS Lambda Powertools</b><br/>
        <code>aws-powertools/powertools-lambda-python</code>
      </td>
      <td>
        <a href="https://github.com/aws-powertools/powertools-lambda-python/pull/8374"><b>#8374</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/><br/>
        <code>+50 / -5</code>
      </td>
      <td>
        <b>OpenAPI Parameter Deduplication:</b> Omitted redundant <code>Content-Type</code> header parameters from generated OpenAPI specifications while preserving runtime media-type validation.
      </td>
    </tr>
    <tr>
      <td>
        <b>Cloudflare Workers SDK</b><br/>
        <code>cloudflare/workers-sdk</code>
      </td>
      <td>
        <a href="https://github.com/cloudflare/workers-sdk/pull/14668"><b>#14668</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/><br/>
        <code>+140 / -1</code>
      </td>
      <td>
        <b>Local Explorer UI Containment:</b> Added responsive vertical scroll containment to the worker selection UI, resolving clipping bugs for multi-worker environments.
      </td>
    </tr>
    <tr>
      <td>
        <b>Apache DataFusion Comet</b><br/>
        <code>apache/datafusion-comet</code>
      </td>
      <td>
        <a href="https://github.com/apache/datafusion-comet/pull/5458"><b>#5458</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white"/><br/>
        <code>+11 / -0</code>
      </td>
      <td>
        <b>Performance Tuning Guide:</b> Documented columnar-to-row (C2R) transition overhead and stage-revert tuning strategies for wide and nested Spark schemas.
      </td>
    </tr>
    <tr>
      <td>
        <b>MUI Material-UI</b><br/>
        <code>mui/material-ui</code>
      </td>
      <td>
        <a href="https://github.com/mui/material-ui/pull/48883"><b>#48883</b></a><br/>
        <img src="https://img.shields.io/badge/Merged-238636?style=flat-square&logo=github&logoColor=white" />
      </td>
      <td>
        <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black"/><br/>
        <code>+32 / -3</code>
      </td>
      <td>
        <b>Slot Prop Inheritance:</b> Documented React <code>Autocomplete</code> slot prop inheritance rules to prevent rendering bugs during multi-select custom input adornment configuration.
      </td>
    </tr>
  </tbody>
</table>

<br/>

### Selected Active Open Pull Requests

| Repository | PR Link | Stack | Technical Focus |
| :--- | :---: | :---: | :--- |
| **Apache DataFusion Ballista**<br/>`apache/datafusion-ballista` | [#2397](https://github.com/apache/datafusion-ballista/pull/2397) | `Rust` `utoipa` `+523 / -26` | OpenAPI v3 specification generator and JSON endpoint for distributed scheduler. |
| **Delta Lake Core**<br/>`delta-io/delta-rs` | [#4685](https://github.com/delta-io/delta-rs/pull/4685) | `Rust` `Parquet` `+43 / -4` | Nested struct field override preservation for DataFusion Parquet leaf pruning. |
| **Hugging Face Safetensors**<br/>`safetensors/safetensors` | [#826](https://github.com/safetensors/safetensors/pull/826) | `Rust` `Python` `+34 / -3` | Strict memory-layout validation rejecting non-C-contiguous NumPy arrays. |
| **Kubernetes Core**<br/>`kubernetes/kubernetes` | [#140791](https://github.com/kubernetes/kubernetes/pull/140791) | `Go` `Kubelet` `+57 / -4` | Pre-allocation bypass for zero-valued device requests in Kubelet Device Manager. |
| **Deno Runtime Core**<br/>`denoland/deno` | [#36532](https://github.com/denoland/deno/pull/36532) | `Rust` `JS` `+52 / -8` | Teardown socket cleanup closing accepted idle HTTP sockets in Node compatibility layer. |
| **Google TensorFlow Core**<br/>`tensorflow/tensorflow` | [#124960](https://github.com/tensorflow/tensorflow/pull/124960) | `C++` `Runtime` `+9 / -1` | Inter-op compute pool handling for negative thread configuration values. |
| **Google TensorFlow Core**<br/>`tensorflow/tensorflow` | [#124959](https://github.com/tensorflow/tensorflow/pull/124959) | `C++` `oneDNN` `+35 / -1` | Rewrite error propagation preventing aborts on invalid quantized pooling attributes. |
| **PyTorch Deep Learning**<br/>`pytorch/pytorch` | [#191876](https://github.com/pytorch/pytorch/pull/191876) | `Python` `torch.compile` `+65 / -3` | Input shape validation for `pixel_shuffle` meta-registrations and compile paths. |
| **Astral uv**<br/>`astral-sh/uv` | [#20855](https://github.com/astral-sh/uv/pull/20855) | `Rust` `+115 / -27` | Staged atomic binary updates on Windows eliminating file-lock permission panics. |
| **Apple CoreMLTools**<br/>`apple/coremltools` | [#2767](https://github.com/apple/coremltools/pull/2767) | `Python` `MIL` `+46 / -5` | MIL compiler validation rejecting symbolic classifier probability shapes. |
| **Electron Core**<br/>`electron/electron` | [#52737](https://github.com/electron/electron/pull/52737) | `C++` `TS` `+37 / -9` | BaseWindow normalization ensuring compliance with `Partial<Rectangle>` bounds. |
| **Vercel Next.js**<br/>`vercel/next.js` | [#96111](https://github.com/vercel/next.js/pull/96111) | `TypeScript` `+40 / -1` | Middleware rewrite search parameter retention in App Router request URLs. |
| **AWS Lambda Rust Runtime**<br/>`aws/aws-lambda-rust-runtime` | [#1162](https://github.com/aws/aws-lambda-rust-runtime/pull/1162) | `Rust` `SNS` `+45 / -2` | Fixed millisecond timestamp precision for SNS signature verification. |
| **Ansible Automation**<br/>`ansible/ansible` | [#87326](https://github.com/ansible/ansible/pull/87326) | `Python` `+224 / -4` | Direct tarball download command in `ansible-galaxy role` for air-gapped systems. |
| **Graphify Knowledge Graph**<br/>`Graphify-Labs/graphify` | [#2728](https://github.com/Graphify-Labs/graphify/pull/2728) | `Python` `+176 / -51` | Windows CLI candidate probing preventing PATH-shadowing subprocess errors. |
| **Graphify Knowledge Graph**<br/>`Graphify-Labs/graphify` | [#2726](https://github.com/Graphify-Labs/graphify/pull/2726) | `Python` `+85 / -17` | Fail-closed artifact preservation during community labeling failures. |
| **Storybook Ecosystem**<br/>`storybookjs/storybook` | [#35520](https://github.com/storybookjs/storybook/pull/35520) | `TypeScript` `+250 / -10` | Angular Signal Query isolation preventing property overwrites in decorators. |
| **Microsoft PowerToys**<br/>`microsoft/PowerToys` | [#49375](https://github.com/microsoft/PowerToys/pull/49375) | `C++` `+56 / -10` | Culture-aware digit formatting for Command Palette calculator results. |
| **Pytest Framework**<br/>`pytest-dev/pytest` | [#14707](https://github.com/pytest-dev/pytest/pull/14707) | `Python` `+69 / -13` | Custom TOML file root table parsing for `pytest -c` executions. |
| **Node Version Manager**<br/>`nvm-sh/nvm` | [#3891](https://github.com/nvm-sh/nvm/pull/3891) | `Shell` `+45 / -0` | Shell trap restoration for Zsh `extendedglob` terminal settings. |
| **Nx Monorepo Toolkit**<br/>`nrwl/nx` | [#36347](https://github.com/nrwl/nx/pull/36347) | `TypeScript` `+409 / -452` | Compiler plugin migration to `minimizer-webpack-plugin` with `cssnano`. |
| **NousResearch Hermes Agent**<br/>`NousResearch/hermes-agent` | [#70711](https://github.com/NousResearch/hermes-agent/pull/70711) | `Python` `+63 / -2` | Local slash command auto-completion support in terminal interface. |
| **NousResearch Hermes Agent**<br/>`NousResearch/hermes-agent` | [#70381](https://github.com/NousResearch/hermes-agent/pull/70381) | `TypeScript` `+175 / -1` | Reactive state refresh hooks for active chat sessions in dashboard UI. |
| **Traceroot AI**<br/>`traceroot-ai/traceroot` | [#1860](https://github.com/traceroot-ai/traceroot/pull/1860) | `TypeScript` `+28 / -12` | Ambiguous filter field glyph replacement with neutral fallback icons. |

<br/>

<details>
<summary><b>Complete Index of All 56 Pull Requests</b></summary>
<br/>

| # | Repository | PR Title | Status | Language |
| :-: | :--- | :--- | :---: | :---: |
| 1 | `pnpm/pnpm` | [fix(resolving-git-resolver): read git package names during resolution (#13059)](https://github.com/pnpm/pnpm/pull/13059) | Merged | Rust |
| 2 | `pnpm/pnpm` | [fix(lockfile): compare equivalent git specifiers (#13056)](https://github.com/pnpm/pnpm/pull/13056) | Merged | Rust |
| 3 | `tensorflow/tensorflow` | [Avoid oneDNN abort for out-of-range convolution attributes (#124961)](https://github.com/tensorflow/tensorflow/pull/124961) | Merged | C++ |
| 4 | `pytorch/pytorch` | [[BE] Fix B018 warnings in symmetric-memory Triton hooks (#191831)](https://github.com/pytorch/pytorch/pull/191831) | Merged | Python |
| 5 | `vitejs/vite` | [fix(build): map CSS chunks in chunk import maps (#22947)](https://github.com/vitejs/vite/pull/22947) | Merged | TypeScript |
| 6 | `PostHog/posthog` | [feat(cli): configure sourcemap upload concurrency (#70314)](https://github.com/PostHog/posthog/pull/70314) | Merged | Rust |
| 7 | `redis/node-redis` | [fix(sentinel): cap post-connect rediscovery retries (#3388)](https://github.com/redis/node-redis/pull/3388) | Merged | TypeScript |
| 8 | `rclone/rclone` | [dropbox: propagate caller contexts to SDK requests (#9712)](https://github.com/rclone/rclone/pull/9712) | Merged | Go |
| 9 | `CERN/TIGRE` | [Fix Varian loader direction and XIM parsing (#762)](https://github.com/CERN/TIGRE/pull/762) | Merged | Python / MATLAB |
| 10 | `deepset-ai/haystack-core-integrations` | [fix: support quantization ranges for int8/uint8 sentence-transformers (#3543)](https://github.com/deepset-ai/haystack-core-integrations/pull/3543) | Merged | Python |
| 11 | `docling-project/docling` | [fix: skip image enrichment without pages (#3875)](https://github.com/docling-project/docling/pull/3875) | Merged | Python |
| 12 | `neovim/neovim` | [fix(ui2): retain substitute confirmation highlight with nohlsearch (#41067)](https://github.com/neovim/neovim/pull/41067) | Merged | C / Lua |
| 13 | `twentyhq/twenty` | [fix: preserve morph-related records when merging people (#23945)](https://github.com/twentyhq/twenty/pull/23945) | Merged | TypeScript |
| 14 | `aws-powertools/powertools-lambda-python` | [fix(event_handler): omit Content-Type header from OpenAPI (#8374)](https://github.com/aws-powertools/powertools-lambda-python/pull/8374) | Merged | Python |
| 15 | `cloudflare/workers-sdk` | [[local-explorer-ui] Fix worker selector scrolling (#14668)](https://github.com/cloudflare/workers-sdk/pull/14668) | Merged | TypeScript |
| 16 | `apache/datafusion-comet` | [docs: document C2R cost for wide/nested schemas in tuning guide (#5458)](https://github.com/apache/datafusion-comet/pull/5458) | Merged | Markdown |
| 17 | `mui/material-ui` | [[docs][autocomplete] Clarify how to render custom start and end adornments (#48883)](https://github.com/mui/material-ui/pull/48883) | Merged | TypeScript |
| 18 | `apache/datafusion-ballista` | [feat(scheduler): document REST API with OpenAPI and serve /api/openapi.json (#2397)](https://github.com/apache/datafusion-ballista/pull/2397) | Open | Rust |
| 19 | `delta-io/delta-rs` | [fix(core): preserve nested schema overrides in parquet read schema (#4685)](https://github.com/delta-io/delta-rs/pull/4685) | Open | Rust |
| 20 | `safetensors/safetensors` | [fix(numpy): reject non-C-contiguous arrays (#826)](https://github.com/safetensors/safetensors/pull/826) | Open | Rust / Python |
| 21 | `kubernetes/kubernetes` | [kubelet: skip zero-valued device requests (#140791)](https://github.com/kubernetes/kubernetes/pull/140791) | Open | Go |
| 22 | `denoland/deno` | [fix(ext/node): close accepted idle HTTP sockets (#36532)](https://github.com/denoland/deno/pull/36532) | Open | Rust / JS |
| 23 | `tensorflow/tensorflow` | [Fix negative inter-op count in compute pool (#124960)](https://github.com/tensorflow/tensorflow/pull/124960) | Open | C++ |
| 24 | `tensorflow/tensorflow` | [Avoid abort on invalid quantized pool attributes (#124959)](https://github.com/tensorflow/tensorflow/pull/124959) | Open | C++ |
| 25 | `pytorch/pytorch` | [Fix pixel_shuffle validation in compile paths (#191876)](https://github.com/pytorch/pytorch/pull/191876) | Open | Python |
| 26 | `astral-sh/uv` | [Stage Windows self-updates before replacing uv.exe (#20855)](https://github.com/astral-sh/uv/pull/20855) | Open | Rust |
| 27 | `apple/coremltools` | [fix(mil): reject symbolic classifier probability shapes (#2767)](https://github.com/apple/coremltools/pull/2767) | Open | Python |
| 28 | `electron/electron` | [fix: support partial BaseWindow bounds (#52737)](https://github.com/electron/electron/pull/52737) | Open | C++ / TS |
| 29 | `vercel/next.js` | [fix(app-router): preserve middleware rewrite query parameters (#96111)](https://github.com/vercel/next.js/pull/96111) | Open | TypeScript |
| 30 | `aws/aws-lambda-rust-runtime` | [Fix SNS timestamp serialization to preserve millisecond precision (#1162)](https://github.com/aws/aws-lambda-rust-runtime/pull/1162) | Open | Rust |
| 31 | `ansible/ansible` | [Add ansible-galaxy role download (#87326)](https://github.com/ansible/ansible/pull/87326) | Open | Python |
| 32 | `Graphify-Labs/graphify` | [fix(llm): probe Windows Claude CLI candidates before spawning (#2728)](https://github.com/Graphify-Labs/graphify/pull/2728) | Open | Python |
| 33 | `Graphify-Labs/graphify` | [fix(cli): preserve graph artifacts when community labeling fails (#2726)](https://github.com/Graphify-Labs/graphify/pull/2726) | Open | Python |
| 34 | `storybookjs/storybook` | [Angular: Preserve Signal Queries When Applying Story Props (#35520)](https://github.com/storybookjs/storybook/pull/35520) | Open | TypeScript |
| 35 | `microsoft/PowerToys` | [[CmdPal] Add number separators to calculator results (#49375)](https://github.com/microsoft/PowerToys/pull/49375) | Open | C++ |
| 36 | `pytest-dev/pytest` | [Fix custom TOML config files passed with -c (#14707)](https://github.com/pytest-dev/pytest/pull/14707) | Open | Python |
| 37 | `nvm-sh/nvm` | [[Fix] Preserve zsh extendedglob when reading aliases (#3891)](https://github.com/nvm-sh/nvm/pull/3891) | Open | Shell |
| 38 | `nrwl/nx` | [fix(webpack): migrate to minimizer-webpack-plugin (#36347)](https://github.com/nrwl/nx/pull/36347) | Open | TypeScript |
| 39 | `NousResearch/hermes-agent` | [fix(tui): complete local slash commands (#70711)](https://github.com/NousResearch/hermes-agent/pull/70711) | Open | Python |
| 40 | `NousResearch/hermes-agent` | [fix(dashboard): refresh chat session switcher (#70381)](https://github.com/NousResearch/hermes-agent/pull/70381) | Open | TypeScript |
| 41 | `traceroot-ai/traceroot` | [fix(ui): distinguish fallback field glyph (#1860)](https://github.com/traceroot-ai/traceroot/pull/1860) | Open | TypeScript |

</details>

---

## Experience & Research

### Samsung R&D Institute India
**PRISM Research Intern (AI Safety & Systems Architecture)** &nbsp;|&nbsp; *April 2025 – September 2025*
* **Encoder-Only Guardrails:** Fine-tuned `ModernBERT-large` (395M parameters) into a lightweight classifier for prompt injection and jailbreak detection across 75k+ augmented adversarial samples (*InjectGuard, BIPIA, NotInject, WildGuard-Benign, PINT*).
* **Latency & Benchmarks:** Reached **92.70% accuracy** and **0.9021 F1-score** on a 315-prompt adversarial benchmark with **35 ms inference latency** (~300x faster than generation-based alternatives), outperforming *NVIDIA NeMo Guardrails, Llama Guard 4, Prompt Guard, and DeBERTa-v3*.
* **Publication:** Co-authored *"AI Guardrails: Performance-Optimized Guardrail System for Secure LLM and Agentic AI Interactions"*, **Accepted to ICSCCC-2026**.

### Indian Institute of Technology Madras
**AI Research & Prototyping Intern (Scientific ML & PINNs)** &nbsp;|&nbsp; *June 2025 – August 2025*
* **Physics-Informed Neural Networks (PINNs):** Embedded biological differential equations directly into PyTorch loss functions for spatiotemporal modeling of Alzheimer's disease progression on longitudinal MRI data.
* **Accuracy Gains:** Implemented automatic differentiation for PDE residuals, collocation sampling, and adaptive loss weighting, delivering a **27% improvement in early neurodegeneration prediction accuracy** over conventional deep learning baselines.

---

## Featured Projects

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait/stratum">Stratum</a></h3>
      <p><b>S3-Compatible Edge Distributed Object Storage</b></p>
      <p><img src="https://img.shields.io/badge/Cloudflare%20Workers-F38020?style=flat-square&logo=cloudflare&logoColor=white"/> <img src="https://img.shields.io/badge/D1%20%7C%20R2%20%7C%20KV-0051C3?style=flat-square"/> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/></p>
      <ul>
        <li>Architected edge S3 object storage achieving <b>95% cost reduction</b> via multi-tier caching (Edge Cache hot reads, R2 warm cache, Telegram Bot cold storage).</li>
        <li>Sub-50ms metadata queries via Cloudflare D1 with SHA-256 and Content-MD5 integrity checks.</li>
        <li>100% compatibility with S3 CLI/SDKs via reverse-engineered S3 XML response serialization.</li>
        <li><b>Demo:</b> <a href="https://stratum.opener.workers.dev">stratum.opener.workers.dev</a></li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait/pulseflare">Pulseflare</a></h3>
      <p><b>Serverless Edge Observability & Incident Intelligence</b></p>
      <p><img src="https://img.shields.io/badge/Workers%20AI-F38020?style=flat-square&logo=cloudflare&logoColor=white"/> <img src="https://img.shields.io/badge/React%20%2B%20Vite-61DAFB?style=flat-square&logo=react&logoColor=black"/> <img src="https://img.shields.io/badge/Hono-E36002?style=flat-square"/></p>
      <ul>
        <li>Serverless edge uptime monitoring maintaining <b>99.99% uptime</b> across distributed endpoints.</li>
        <li>Decoupled 1-min health checks from AI anomaly analysis via Cloudflare Queues for zero latency impact.</li>
        <li>Integrated Workers AI (<code>LLaMA-3.1-8B</code>) for automated root-cause summaries, reducing MTTR by <b>70%</b>.</li>
        <li><b>Demo:</b> <a href="https://pulseflare.pages.dev">pulseflare.pages.dev</a></li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait/ShopLense">ShopLense</a></h3>
      <p><b>Hyperlocal Quick-Commerce Price Intelligence</b></p>
      <p><img src="https://img.shields.io/badge/Next.js%2015-000000?style=flat-square&logo=next.js&logoColor=white"/> <img src="https://img.shields.io/badge/React%2019-61DAFB?style=flat-square&logo=react&logoColor=black"/> <img src="https://img.shields.io/badge/Prisma%20%2B%20Neon-3982CE?style=flat-square"/></p>
      <ul>
        <li>Aggregated live inventory & pricing across Zepto, Blinkit, Instamart, and Flipkart Minutes with <b>85% discovery speedup</b>.</li>
        <li>Reverse-engineered marketplace protocols with custom Node scrapers maintaining <b>99.8% extraction accuracy</b>.</li>
        <li>Mapped 10k+ SKUs into unified groups via token similarity algorithms; scheduled 5,000+ daily alert checks.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait/WoundDoc">WoundDoc</a></h3>
      <p><b>Edge AI Clinical Diagnostics System</b></p>
      <p><img src="https://img.shields.io/badge/TensorFlow%20Lite-FF6F00?style=flat-square&logo=tensorflow&logoColor=white"/> <img src="https://img.shields.io/badge/React%20Native-61DAFB?style=flat-square&logo=react&logoColor=black"/> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square"/></p>
      <ul>
        <li>Hybrid MiT-b3 + CNN + P-scSE segmentation achieving <b>92.33% classification accuracy</b> and <b>87.64% Dice</b>.</li>
        <li>Quantized 16-class EfficientNet-B0 to TFLite (48 MB &rarr; 12.5 MB) for low-end mobile SoCs (Snapdragon 439).</li>
        <li>Validated in 28-day clinical pilot across 2 Tamil Nadu rural clinics (4.7% area error vs calipers). <b>Submitted to MIDL 2026</b>.</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait">OnyxBin</a></h3>
      <p><b>Distributed Metadata-First Cloud Storage Engine</b></p>
      <p><img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white"/> <img src="https://img.shields.io/badge/Telethon-2CA5E0?style=flat-square"/></p>
      <ul>
        <li>Separated Postgres metadata from binary chunks stored via Telegram MTProto API, achieving <b>81% storage cost savings</b>.</li>
        <li>Adaptive 20 MB chunking with SHA-256 integrity; handled 1,240+ operations over 6-week beta with <b>zero data loss</b>.</li>
        <li>Server-signed HMAC-SHA256 request authorization with sub-42ms metadata API responses.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/DebadityaHait">FluencyRecap</a></h3>
      <p><b>Vernacular & Non-Native English ASR Pipeline</b></p>
      <p><img src="https://img.shields.io/badge/OpenAI%20Whisper-412991?style=flat-square&logo=openai&logoColor=white"/> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"/> <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square"/></p>
      <ul>
        <li>Fine-tuned Whisper on 180+ hrs Indian English and 62 hrs Hinglish audio, yielding a <b>22% reduction in Word Error Rate</b>.</li>
        <li>91% accuracy in detecting disfluencies (fillers, backtracking) with sub-280ms CPU inference across 650+ practice sessions.</li>
        <li>Deployed to 47 non-native speakers, delivering 37% average reduction in filler words over 3 months.</li>
      </ul>
    </td>
  </tr>
</table>

---

## Competitive Programming & Hackathons

<div align="center">

| Platform / Event | Distinction | Standing |
| :--- | :--- | :--- |
| **LeetCode** | **Guardian** | **Top 2% Globally** |
| **Codeforces** | **Expert** | Peak *Candidate Master* |
| **CodeChef** | **4-Star Coder** | Division 1 Competitor |
| **Goldman Sachs Hackathon 2026** | **All-India Rank 42** (Quant Track) | **Top ~0.3%** of ~14,000 participants |
| **Goldman Sachs Hackathon 2026** | **All-India Rank 144** (CS Track) | **Top ~0.9%** of 15,953 participants |
| **Amazon ML Summer School 2026** | **Selected Scholar** | **Top 2.2%** (Top 3,000 of 134,000+ applicants) |
| **Flipkart GRiD 8.0 (2026)** | **National Semifinalist** (Software Dev) | **Top ~2.3%** of 130,000+ applicants |
| **Flipkart GRiD 7.0 (2025)** | **National Semifinalist** (Software Dev) | Selected among **160,000+ participants** |
| **Adobe India Hackathon 2025** | **National Semifinalist** (Creator of *Outlinr*) | Selected from **260,000 registrations** |
| **Founder’s Scholarship** | **Full Academic Merit Scholarship** | SRM Institute of Science and Technology (2023) |

</div>

---

## Certifications

<div align="center">

| Issuer | Credential Title | Verification ID |
| :--- | :--- | :--- |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Fabric Data Engineer Associate** | `2CFE44AF9A03CA00` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure Data Scientist Associate** | `6B609B2E62C7DD1B` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure Developer Associate** | `7C24709582312829` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure AI Engineer Associate** | `C6A78B398CD5D2CE` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Fabric Analytics Engineer Associate** | `31C332B22EA60C45` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Power BI Data Analyst Associate** | `AB65FD5A69BEE6C9` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure Fundamentals** | `C98BA2EF3EA717B0` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure Data Fundamentals** | `A05553E0E826BF55` |
| <img src="https://img.shields.io/badge/Microsoft-0078D4?style=flat-square&logo=microsoft&logoColor=white" /> | **Microsoft Certified: Azure AI Fundamentals** | `743A61D9C9700E53` |
| <img src="https://img.shields.io/badge/Anthropic-D97706?style=flat-square&logo=anthropic&logoColor=white" /> | **Claude Certified Architect - Foundations** | Anthropic Verified |
| <img src="https://img.shields.io/badge/Oracle-F80000?style=flat-square&logo=oracle&logoColor=white" /> | **OCI Certified AI Foundations Associate** | Oracle Cloud Verified |
| <img src="https://img.shields.io/badge/DeepLearning.AI-00A4E4?style=flat-square" /> | **Machine Learning Specialization** | Stanford / DeepLearning.AI |

</div>

---

## Technical Skills

<div align="center">

```
========================================================================================================
  CORE LANGUAGES       ::  Rust  •  C / C++  •  Python  •  TypeScript  •  Go  •  SQL  •  JavaScript
  SYSTEMS & RUNTIMES   ::  Deno  •  Node.js  •  Linux Kernel APIs  •  oneDNN  •  Triton  •  Electron
  AI / ML / TENSORS    ::  PyTorch  •  TensorFlow  •  TFLite  •  Hugging Face  •  Safetensors  •  PINNs
  EDGE & CLOUDFLARE    ::  Cloudflare Workers  •  D1  •  R2  •  KV  •  Queues  •  Workers AI  •  Pages
  BACKEND & STORAGE    ::  FastAPI  •  Next.js App Router  •  PostgreSQL / Neon  •  Prisma  •  Redis  •  S3
  DEV TOOLS & DEVOPS   ::  Git  •  Docker  •  Wrangler  •  Rollup / Vite  •  pnpm  •  uv  •  Pytest  •  Vitest
========================================================================================================
```

</div>

<p align="center">
  <!-- Languages -->
  <img src="https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white"/>
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white"/>
  <!-- AI / ML -->
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
  <!-- Cloud & Edge -->
  <img src="https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white"/>
</p>

---

## Education

* **SRM Institute of Science and Technology, Kattankulathur, Tamil Nadu**  
  *BTech in Computer Science and Engineering* (2023 – Present) &nbsp;•&nbsp; **CGPA: 8.5 / 10.0**  
  *Focus:* Computer Architecture, Operating Systems, Data Structures & Algorithms, Distributed Systems, AI Systems Architecture.

* **Indian Institute of Technology Madras**  
  *BS in Data Science and Applications* (2024 – Present)

---

## GitHub Activity & Stats

<div align="center">

<a href="https://github.com/debadityahait">
  <img src="https://github-profile-trophy.vercel.app/?username=debadityahait&theme=onedark&no-frame=true&no-bg=true&margin-w=4" alt="GitHub Trophies" />
</a>

<br/><br/>

<table border="0">
  <tr>
    <td>
      <img src="https://github-readme-stats.vercel.app/api?username=debadityahait&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true" alt="Debaditya's GitHub Stats" />
    </td>
    <td>
      <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=debadityahait&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
    </td>
  </tr>
  <tr>
    <td colspan="2" align="center">
      <img src="https://github-readme-streak-stats.herokuapp.com/?user=debadityahait&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
    </td>
  </tr>
</table>

</div>

---

## Contact

<div align="center">

<p align="center">
  <a href="https://linkedin.com/in/debadityahait">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Connect" />
  </a>
  &nbsp;
  <a href="mailto:debaditya2005hait@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-Send%20Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Send Email" />
  </a>
  &nbsp;
  <a href="https://github.com/debadityahait">
    <img src="https://img.shields.io/badge/GitHub-Follow%20@debadityahait-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Follow" />
  </a>
</p>

<!-- Footer Wave -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&custom_color_list=30,5,2,2,0&height=100&section=footer" width="100%" alt="Footer Wave" />

</div>
