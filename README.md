# LLM_Project
To create a sentiment analysis with the use of large lnaguage model to analyse the emotions related to IMDB movie reviews.

## Dataset
Large Movie Review Dataset from Huggingface.co. This is a dataset for binary sentiment classification containing substantially more data than previous benchmark datasets. They provided a set of 25,000 highly polar movie reviews for training, and 25,000 for testing.
[Link to Dataset Here](https://huggingface.co/lvwerra/distilbert-imdb)


## Based Model
I used the Random Forest Classification model to calculate the accuracy of the classification lable column that was included on the IMDB Movie Dataset. The RAM kept stopping because of how large the dataset was.

## Pre-trained Model 
See the **OptimizedModel** nptebook. I used the "distilbert-base-uncase' model from Huggingface.co. 
[Link to Model Here](https://huggingface.co/distilbert/distilbert-base-uncased)

## Performance Metrics
`
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],
    compute_metrics=compute_metrics
)
`
The model had an accurcy of 0.928. The total training time lasted about 1 hour and 22 minutes using Google CoLab.