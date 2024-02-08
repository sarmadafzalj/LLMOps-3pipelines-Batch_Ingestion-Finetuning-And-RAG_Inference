# LLMOps: Feature | Inference | Finetune - 3Pipeline Architecture for LLM Based RAG Application on Tech News Architecture

**Transform your private LLM into an expert by utilizing a carefully curated dataset leveraging state-of-the-art GPT-4 and then fine-tuning with LLama2 7B.**
<table>
    <tr>
        <td width = 30%>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <p><h3>Application Overview</h3></p>
            <p>Every morning 9AM CST, fetch latest articles from Aylien tech news API. Chunk, embed and load into Vectara database and using OpenAI GPT-4 created a curated Q/A set for finetuning. Serve the on with Inference pipeline which query the vectors from Vectara database and synthesize with your privately hosted LLama2 7B. With a good amount of QA set generated with diverse articles run Fine-tuning pipeline every month and employ CI/CD to deploy updated model weights into production. Down the line in 6 months, the small LLama2 is your new expert with specialization in understanding Tech and its jargon.</p>
        </td>
    </tr>
</table>

## Objective
Automated pipelines for feature store, inference and finetuning for making your compact and private LLM (LLama2 7B) an expert on Technology. It leverages GPT-4 to curate Q/A dataset whcih is then used to finetune the LLama2 and then down the line Q/A extraction is be stopped once we have optimal responses from Llama2.

## Tech-Stack
<table>
    <tr>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
    </tr>
    <tr>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <p><b>Llama-Index</b></p>
            <p>Framework for ingestion and RAG orchestration</p>
        </td>
        <td>
            <img src="Images\trainingrobot.jpeg" alt="Your Image">
        </td>
    </tr>
</table>