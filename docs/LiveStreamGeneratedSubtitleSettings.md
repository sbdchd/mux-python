# LiveStreamGeneratedSubtitleSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name for this live stream subtitle track. | [optional] 
**passthrough** | **str** | Arbitrary metadata set for the live stream subtitle track. Max 255 characters. | [optional] 
**language_code** | **str** | The language to generate subtitles in. | [optional] [default to 'en']
**transcription_vocabulary_ids** | **list[str]** | Unique identifiers for existing Transcription Vocabularies to use while generating subtitles for the live stream. If the Transcription Vocabularies provided collectively have more than 1000 phrases, only the first 1000 phrases will be included. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


